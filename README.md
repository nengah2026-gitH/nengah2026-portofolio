# Data Analyst Portfolio - 30 Days Challenge
Repo ini berisi project harian gue buat belajar Data Analyst dari nol sampai bisa bikin dashboard.

---

### Day 1: SQL Basics
Belajar query dasar SQL buat analisis data penjualan.

**Yang dikerjain:**
1. SELECT, WHERE, ORDER BY, GROUP BY
2. JOIN 2 tabel: orders & customers
3. Agregasi total penjualan per bulan

**Tools**
- PostgreSQL
- DBeaver

---

### Day 2: Python Pandas Fundamentals
Eksplorasi data CSV pakai Pandas.

**Yang dikerjain:**
1. Load dan cleaning data kotor
2. Filter data berdasarkan kondisi
3. Bikin kolom baru dan grouping

**Tools**
- Python
- Pandas
- Jupyter Notebook

---

### Day 3: Data Visualization with Python
Visualisasi data penjualan biar gampang dibaca.

**Yang dikerjain:**
1. Load data pakai pandas
2. Bikin Bar Chart untuk total penjualan per produk
3. Bikin Line Chart untuk tren penjualan bulanan

**Tools**
- Python
- Pandas
- Matplotlib
- Seaborn
- Google Colab

---

### Day 4: Sales Data Automation with Python
Otomasi laporan penjualan bulanan pakai Python.

**Yang dikerjain:**
1. Auto load data dari Excel
2. Generate grafik tren penjualan
3. Export hasil ke folder laporan

**Tools**
- Python
- Pandas
- Openpyxl
- Matplotlib
  
### Day 5: Analisis Penjualan dengan Python

**Yang dikerjain:**
1. Load file penjualan.csv pakai pandas di Google Colab
2. Group data buat cari produk terlaris
3. Baca hasil analisis dan bikin kesimpulan

**Hasil:**
- Produk Ebook Copywriting & Template IG paling banyak terjual (3x)
- Total pendapatan tertinggi dari Ebook Copywriting
- Task selesai dalam 15 menit
  
  ## Day 6 - Tren Penjualan per Bulan 📈

Hari ini gue bikin grafik buat liat tren penjualan dari bulan ke bulan pakai data yang sama kayak Day 5.
[Lihat Notebook Day 6](day6_tren_penjualan%20(1).ipynb)

### Yang dikerjain:
- Ubah kolom `Tanggal` jadi format datetime biar bisa di-group per bulan
- Pakai `groupby` + `dt.to_period('M')` buat ngitung total penjualan tiap bulan
- Plot hasil jadi grafik garis pakai matplotlib

### Hasil:
Grafik garis yang nunjukin penjualan naik/turun tiap bulan. Jadi lebih gampang liat pola musiman atau bulan yang performanya jelek.

### File:
- [Lihat Notebook Day 6](../day6_tren_penjualan%20(1).ipynb)
- [Data CSV](./Day5_analisis/data_penjualan_day1.csv)
