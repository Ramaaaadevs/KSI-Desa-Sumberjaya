# 📁 Sistem Arsip & Templating Surat - Desa Sumberjaya

> **Sistem manajemen surat desa dengan fitur templating otomatis dan generate PDF dengan kop surat profesional**

[![Laravel](https://img.shields.io/badge/Laravel-11.46-red.svg)](https://laravel.com)
[![PHP](https://img.shields.io/badge/PHP-8.3-blue.svg)](https://php.net)
[![Filament](https://img.shields.io/badge/Filament-3.2-orange.svg)](https://filamentphp.com)

---

## 🎯 Fitur Utama

### 📝 Arsip Surat (Unified)
- **Buat Surat dari Template** → Auto generate PDF dengan kop surat
- **Input Manual** → Upload surat existing/scan dokumen
- Kategori surat (Masuk/Keluar)
- Status tracking (Draft, Terkirim, Diarsipkan, Selesai)
- Download & Print pdf

### 📄 Template Surat
- Template builder dengan Rich Text Editor
- Variable system untuk data dinamis
- Pengaturan margin & layout
- Kop surat otomatis dari Pengaturan Desa
- Preview template real-time

### ⚙️ Pengaturan Desa
- Data lengkap desa/kecamatan/kabupaten/provinsi
- Upload logo desa untuk kop surat
- Informasi kontak & alamat
- Data pejabat penandatangan default
- 30+ variable tersedia untuk template

### 📊 Kategori Surat
- Manajemen kategori surat
- Warna badge custom per kategori
- Tracking jumlah surat per kategori

---

## 🚀 Quick Start

### Prerequisites
- PHP 8.3+
- Composer
- MySQL/MariaDB
- Node.js & NPM

### Installation

```bash
# Clone repository
git clone https://github.com/cengkooo/arsip-templating-surat-sumberjaya-ksi-rb-5.git
cd arsip-templating-surat-sumberjaya-ksi-rb-5

# Install dependencies
composer install
npm install

# Setup environment
cp .env.example .env
php artisan key:generate

# Database setup
php artisan migrate --seed
# Seeder otomatis akan membuat akun admin + seluruh template contoh (SKTM, Domisili, SKU, SKK) + Pengaturan Desa default

# Link storage
php artisan storage:link

# Run development server
php artisan serve
npm run dev
```

### Default Login
```
Email: admindesa@sumberjaya.com
Password: password
```

---

## Link Penting
1. spreadsheet data ksi: https://docs.google.com/spreadsheets/d/15wv0C9RP7HcKJzXWTkF-kZid1zG5Ff04Y6dlHKU-9nE/edit?gid=0#gid=0
2. proposal : https://docs.google.com/document/d/1wA6uCeQf3gpBvlBmxeLnwY1lu-z9w_Igid8YPH-R2gg/edit?usp=sharing
3. ppt proposal 1 ( download jadiin pdf dari canva): https://www.canva.com/design/DAGza0wgDgg/bY1CPBoQq8Ac5I0Ztie13g/edit
4. dokumentasi uts ksi: https://drive.google.com/drive/folders/1slNEItA_eSq25cPtnK62zz2staQsL_8Y
5. hasil video uts: https://drive.google.com/file/d/1z3VArV3tqUhL2PD_bttvYZGIWIPwJjmL/view
6. ppt 1 : (https://www.canva.com/design/DAGza0wgDgg/bY1CPBoQq8Ac5I0Ztie13g/edit)
7. ppt 2 : https://www.canva.com/design/DAG2r_bbQX0/x-xPzzaDWk_I23a63h6dbw/edit
8. ppt 3 : https://www.canva.com/design/DAGza0wgDgg/bY1CPBoQq8Ac5I0Ztie13g/edit?utm_content=DAGza0wgDgg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
9. Poster : https://www.canva.com/design/DAG5Ip7tWp0/Cy4I6EsWqtr-aG4ixXD-eg/edit?utm_co
10. link repo github: https://github.com/Ramaaaadevs/KSI-Desa-Sumberjaya

## 📚 Dokumentasi

- [📖 TUTORIAL-LENGKAP.md](TUTORIAL-LENGKAP.md) - **Tutorial lengkap step-by-step dari awal**
- [✨ PANDUAN-EDITOR-ADVANCED.md](PANDUAN-EDITOR-ADVANCED.md) - **Panduan Editor TinyMCE (indentasi, formatting, tips & trik)**
- [📖 PANDUAN-ARSIP-SURAT.md](PANDUAN-ARSIP-SURAT.md) - Panduan lengkap penggunaan Arsip Surat
- [📖 PANDUAN-PENGATURAN-DESA.md](PANDUAN-PENGATURAN-DESA.md) - Setup Pengaturan Desa
- [📖 PANDUAN-UPLOAD-LOGO.md](PANDUAN-UPLOAD-LOGO.md) - Cara upload logo kop surat
- [🎨 PANDUAN-CUSTOM-KOP-SURAT.md](PANDUAN-CUSTOM-KOP-SURAT.md) - Customize kop surat format & layout
- [🔄 MIGRASI-DATA-GENERATE-SURAT.md](MIGRASI-DATA-GENERATE-SURAT.md) - Panduan migrasi data lama
- [🧪 BLACKBOX-TESTING-GUIDE.md](BLACKBOX-TESTING-GUIDE.md) - Testing guide dengan 7 scenario
- [🔧 SOLUSI-FINAL-TEXTINPUT.md](SOLUSI-FINAL-TEXTINPUT.md) - Solusi field dropdown/date → TextInput
- [🔧 FIX-DROPDOWN-FIELDS.md](FIX-DROPDOWN-FIELDS.md) - Technical fix untuk field binding
- [🔧 FIX-LOGO-TIDAK-MUNCUL.md](FIX-LOGO-TIDAK-MUNCUL.md) - Troubleshooting logo di PDF

---

## 🎨 Workflow Generate Surat

```
1. Setup Pengaturan Desa
   ↓
2. Buat Template Surat (dengan variable)
   ↓
3. Buat Surat dari Template
   ↓
4. Isi Form Dinamis
   ↓
5. Generate PDF Otomatis ✅
   ↓
6. Tersimpan di Arsip Surat
```

---

## 🔧 Tech Stack

### Backend
- **Laravel 11.46** - PHP Framework
- **Filament 3.2** - Admin Panel
- **DomPDF** - PDF Generator
- **MySQL** - Database

### Frontend
- **Alpine.js** - Reactive framework (via Filament)
- **TailwindCSS** - Styling (via Filament)
- **Livewire** - Dynamic UI

### Packages
- `filament/filament` - Admin panel builder
- `barryvdh/laravel-dompdf` - PDF generation
- `mohamedsabil83/filament-forms-tinyeditor` - Rich text editor
- `spatie/laravel-backup` - Backup management

---

## 📁 Struktur Database

### Tabel Utama
- `users` - User management
- `kategoris` - Kategori surat
- `template_surats` - Template surat
- `arsip_surats` - Arsip surat (unified generate + arsip)
- `desa_settings` - Pengaturan desa (singleton)

### Relasi
```
arsip_surats
  ├── belongsTo → kategoris
  ├── belongsTo → template_surats
  └── belongsTo → users

template_surats
  └── belongsTo → kategoris

desa_settings (singleton)
```

---

## 🎯 Menu Sistem

### Master Data
- **Kategori Surat** - Manajemen Kategori
- **Template Surat** - Template Builder
- **Pengaturan Desa** - Setup Desa

### Surat
- **Arsip Surat** - Generate & arsip (unified)
  - 🟢 Buat Surat dari Template
  - ⚪ Tambah Surat Manual

### Manajemen
- **Pengguna** - User management

---

## ⚠️ Perubahan Sistem

### ❌ Deprecated
- **Menu Generate Surat** - Sudah digabung ke Arsip Surat
- Tidak bisa generate PDF dari menu lama
- Data lama tetap ada, bisa dimigrate

### ✅ Sistem Baru
- **Arsip Surat** dengan 2 fitur:
  1. Generate dari template (auto PDF)
  2. Input manual (upload file)
- Workflow lebih simple dan unified

Lihat [MIGRASI-DATA-GENERATE-SURAT.md](MIGRASI-DATA-GENERATE-SURAT.md) untuk detail.

---

## 🐛 Troubleshooting

### Logo tidak muncul di PDF
Lihat [FIX-LOGO-TIDAK-MUNCUL.md](FIX-LOGO-TIDAK-MUNCUL.md)

### PDF gagal generate
1. Cek `storage/logs/laravel.log`
2. Pastikan Pengaturan Desa sudah terisi
3. Pastikan template sudah aktif
4. Gunakan tombol "Generate Ulang PDF"

### Error 500 saat upload
1. Cek permission folder `storage/`
2. Jalankan `php artisan storage:link`
3. Cek max upload size di `php.ini`

---

## 📞 Support

Untuk bantuan lebih lanjut:
- Baca dokumentasi di folder root
- Cek file PANDUAN-*.md
- Review code comments

---

## 📄 License

This project is proprietary software for Desa Sumberjaya.

---

## 👥 Credits

**Developer:** KSI Rekayasa Bangun  
**Client:** Desa Sumberjaya  
**Framework:** Laravel by Taylor Otwell  
**Admin Panel:** Filament by Dan Harrin

---

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

You may also try the [Laravel Bootcamp](https://bootcamp.laravel.com), where you will be guided through building a modern Laravel application from scratch.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains thousands of video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the [Laravel Partners program](https://partners.laravel.com).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[WebReinvent](https://webreinvent.com/)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[DevSquad](https://devsquad.com/hire-laravel-developers)**
- **[Jump24](https://jump24.co.uk)**
- **[Redberry](https://redberry.international/laravel/)**
- **[Active Logic](https://activelogic.com)**
- **[byte5](https://byte5.de)**
- **[OP.GG](https://op.gg)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
