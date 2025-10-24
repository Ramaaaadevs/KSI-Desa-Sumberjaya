import os
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

# --- 1. KONFIGURASI APLIKASI DAN DATABASE ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arsip.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ARCHIVE_FOLDER = 'arsip'
app.config['ARCHIVE_FOLDER'] = ARCHIVE_FOLDER
os.makedirs(ARCHIVE_FOLDER, exist_ok=True)


# --- 2. MODEL DATABASE ---
# Model untuk Arsip Dokumen (File Upload)
class Dokumen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_arsip = db.Column(db.String(255), nullable=False, unique=True)
    nama_dokumen = db.Column(db.String(100))
    nik_dokumen = db.Column(db.String(20))
    kategori = db.Column(db.String(50))
    tanggal_upload = db.Column(db.DateTime, default=datetime.utcnow)

# Model untuk Manajemen Surat (Data dari Form)
class Surat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomor_surat = db.Column(db.String(100), unique=True, nullable=False)
    jenis_surat = db.Column(db.String(100))
    nama_pemohon = db.Column(db.String(100))
    nik_pemohon = db.Column(db.String(20))
    keperluan = db.Column(db.Text)
    tanggal_dibuat = db.Column(db.DateTime, default=datetime.utcnow)


# --- 3. RUTE UTAMA & DASHBOARD ---

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# --- 4. RUTE-RUTE UNTUK FITUR ARSIP DIGITAL ---

@app.route('/arsip-digital')
def arsip_digital():
    semua_dokumen = Dokumen.query.order_by(Dokumen.tanggal_upload.desc()).all()
    return render_template('arsip.html', documents=semua_dokumen)

@app.route('/tambah-arsip', methods=['GET', 'POST'])
def tambah_arsip():
    if request.method == 'POST':
        file = request.files.get('file'); kategori = request.form.get('kategori'); nama_input = request.form.get('nama_dokumen', 'TANPA_NAMA').strip(); nik_input = request.form.get('nik_dokumen', '').strip()
        if not file or file.filename == '': return "Error: Tidak ada file yang dipilih.", 400
        if not nik_input: nik_input = None
        final_kategori = kategori
        if kategori == 'LAINNYA':
            kategori_lainnya_value = request.form.get('kategori_lainnya', '').strip().upper()
            if kategori_lainnya_value: final_kategori = kategori_lainnya_value.replace(" ", "_")
        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S'); nama_file_safe = nama_input.upper().replace(" ", "_"); ext = os.path.splitext(file.filename)[1]
        new_filename = f"{final_kategori}_{nama_file_safe}_{timestamp}{ext}"
        file.save(os.path.join(app.config['ARCHIVE_FOLDER'], new_filename))
        dokumen_baru = Dokumen(nama_arsip=new_filename, nama_dokumen=nama_input, nik_dokumen=nik_input, kategori=final_kategori)
        db.session.add(dokumen_baru); db.session.commit()
        return redirect(url_for('arsip_digital'))
    return render_template('tambah_arsip.html')

@app.route('/api/search')
def search_api():
    query = request.args.get('q', '').strip()
    if not query: return jsonify([])
    pattern = f"%{query}%"
    hasil = Dokumen.query.filter(or_(Dokumen.nama_dokumen.like(pattern), Dokumen.nik_dokumen.like(pattern), Dokumen.kategori.like(pattern))).limit(20).all()
    return jsonify([{"nama_arsip": doc.nama_arsip, "kategori": doc.kategori} for doc in hasil])

@app.route('/arsip/<filename>')
def serve_archived_file(filename):
    return send_from_directory(app.config['ARCHIVE_FOLDER'], filename)


# --- 5. RUTE-RUTE UNTUK FITUR MANAJEMEN SURAT ---

@app.route('/manajemen-surat', methods=['GET', 'POST'])
def manajemen_surat():
    if request.method == 'POST':
        jenis = request.form.get('jenis_surat'); nama = request.form.get('nama_pemohon').strip(); nik = request.form.get('nik_pemohon', '').strip(); keperluan = request.form.get('keperluan', '').strip()
        today_str = datetime.now().strftime('%Y-%m-%d')
        count_today = Surat.query.filter(db.func.date(Surat.tanggal_dibuat) == datetime.now().date()).count() + 1
        nomor_surat = f"{jenis.upper()}/{today_str}/{str(count_today).zfill(3)}"
        surat_baru = Surat(nomor_surat=nomor_surat, jenis_surat=jenis, nama_pemohon=nama, nik_pemohon=nik if nik else None, keperluan=keperluan)
        db.session.add(surat_baru); db.session.commit()
        return redirect(url_for('lihat_arsip_surat', id=surat_baru.id))
    return render_template('surat.html')

@app.route('/api/search-surat')
def search_surat_api():
    query = request.args.get('q', '').strip()
    if not query: return jsonify([])
    pattern = f"%{query}%"
    hasil = Surat.query.filter(or_(Surat.nama_pemohon.like(pattern), Surat.nik_pemohon.like(pattern), Surat.nomor_surat.like(pattern))).order_by(Surat.tanggal_dibuat.desc()).limit(20).all()
    return jsonify([{"id": s.id, "nomor_surat": s.nomor_surat, "nama_pemohon": s.nama_pemohon, "jenis_surat": s.jenis_surat} for s in hasil])

@app.route('/surat/arsip/<int:id>')
def lihat_arsip_surat(id):
    data_surat = Surat.query.get_or_404(id)
    return render_template('arsip_surat.html', surat=data_surat)


# --- 6. MENJALANKAN APLIKASI ---
if __name__ == '__main__':
    with app.app_context():
        # Perintah ini akan membuat tabel 'dokumen' dan 'surat' jika belum ada
        db.create_all()
    app.run(debug=True, port=5500)