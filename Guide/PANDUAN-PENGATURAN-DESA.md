# 🏛️ Panduan Pengaturan Desa

## Fitur Pengaturan Desa (OpenSID Style)

Sistem ini menyediakan fitur **Pengaturan Desa** yang lengkap, mirip dengan OpenSID. Data dari pengaturan desa akan **otomatis tersedia** sebagai variable di template surat.

---

## 📋 Cara Mengakses

1. Login ke admin panel
2. Klik menu **Master Data** → **Pengaturan Desa**
3. Klik **Edit** untuk mengubah data

---

## 🗂️ Tab-Tab Pengaturan

### 1. **DESA**
- Upload **Logo Desa/Kabupaten** (untuk kop surat)
- Nama Desa
- Kode Desa (contoh: 18.04.01.2003)
- Kode Pos Desa

### 2. **KECAMATAN**
- Nama Kecamatan
- Kode Kecamatan
- Nama Kepala Camat
- NIP Camat

### 3. **KABUPATEN**
- Nama Kabupaten/Kota
- Kode Kabupaten
- Nama Bupati/Walikota
- NIP Bupati/Walikota

### 4. **PROVINSI**
- Nama Provinsi
- Kode Provinsi

### 5. **Alamat & Kontak**
- Alamat Kantor Desa (lengkap)
- Kode Pos Kantor
- Nomor Telepon
- Email Desa
- Website Desa
- **Koordinat GPS** (Latitude & Longitude)

### 6. **Pejabat**
- Data Kepala Desa (nama & NIP)
- **Pamong TTD Default** → Akan otomatis terisi saat generate surat

---

## 🎯 Variable yang Tersedia di Template

### **Variable Otomatis dari Pengaturan Desa**

Semua data di Pengaturan Desa bisa dipakai sebagai variable:

#### Identitas Wilayah:
```
{{nama_desa}}
{{kode_desa}}
{{nama_kecamatan}}
{{kode_kecamatan}}
{{nama_kabupaten}}
{{kode_kabupaten}}
{{nama_provinsi}}
{{kode_provinsi}}
```

#### Alamat & Kontak:
```
{{alamat_desa}}
{{kode_pos}}
{{kode_pos_desa}}
{{telepon_desa}}
{{email_desa}}
{{website_desa}}
{{latitude}}
{{longitude}}
```

#### Pejabat:
```
{{nama_kepala_desa}}
{{nip_kepala_desa}}
{{nama_kepala_camat}}
{{nip_kepala_camat}}
{{nama_kepala_kabupaten}}
{{nip_kepala_kabupaten}}
{{nama_pamong_ttd}}
{{jabatan_pamong_ttd}}
{{nip_pamong_ttd}}
```

#### Helper KOP Surat:
```
{{identitas_pemerintahan}}  → Nama Kabupaten + Kecamatan + Desa (3 baris)
{{alamat_lengkap}}          → Alamat + Kode Pos
```

---

## 📝 Contoh Penggunaan di Template

### **Header (Kop Surat)**
```html
<div style="text-align: center;">
    <h2>{{nama_kabupaten}}</h2>
    <h3>{{nama_kecamatan}}</h3>
    <h3>{{nama_desa}}</h3>
    <hr>
    <p>{{alamat_lengkap}}</p>
    <p>Telp: {{telepon_desa}} | Email: {{email_desa}}</p>
</div>
```

### **Body (Isi Surat)**
```html
<p>Yang bertanda tangan di bawah ini Kepala {{nama_desa}}, {{nama_kecamatan}}, 
{{nama_kabupaten}}, {{nama_provinsi}} menerangkan bahwa:</p>

<p>Nama: {{nama}}</p>
<p>NIK: {{nik}}</p>
```

### **Footer (Tanda Tangan)**
```html
<div style="text-align: right;">
    <p>{{nama_desa}}, {{tanggal_surat}}</p>
    <p>{{jabatan}}</p>
    <br><br><br>
    <p><strong><u>{{penandatangan}}</u></strong></p>
    <p>NIP: {{nip}}</p>
</div>
```

---

## 🔄 Alur Kerja

1. **Set Pengaturan Desa** → Isi data lengkap di menu Pengaturan Desa
2. **Buat Template Surat** → Gunakan variable dari Pengaturan Desa
3. **Generate Surat** → Data otomatis terambil dari Pengaturan Desa + Form Isian
4. **PDF Final** → Kop surat otomatis tampil dengan logo dan data desa

---

## ⚡ Keuntungan

✅ **Sekali Setup** → Data desa hanya perlu diisi 1x  
✅ **Otomatis Tersedia** → Semua template bisa akses data desa  
✅ **Konsisten** → Kop surat selalu sama di semua surat  
✅ **Fleksibel** → Bisa override penandatangan per surat  
✅ **Logo Otomatis** → Logo tampil otomatis di PDF  

---

## 🚀 Update Data Desa

Jika ada perubahan:
- **Nama Kepala Desa** → Update di Pengaturan Desa
- **Alamat** → Update di Pengaturan Desa
- **Logo** → Upload ulang di Pengaturan Desa

Semua surat yang **belum digenerate** akan otomatis pakai data terbaru!

---

## 📞 Variable Tambahan

Selain variable dari Pengaturan Desa, Anda juga bisa tambahkan variable custom di **Tab Form Isian** saat buat template. Variable custom ini akan muncul sebagai form isian saat Generate Surat.

**Contoh:**
- {{nama}} → Form isian Nama
- {{nik}} → Form isian NIK
- {{alamat}} → Form isian Alamat
- dll

---

Selamat menggunakan GOOD! 🎉
