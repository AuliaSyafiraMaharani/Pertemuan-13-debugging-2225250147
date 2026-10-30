# Pertemuan 13 - Debugging dan Testing

Nama: Aulia Syafira Maharani 
NIM: 2225250147
Kelas: 3A  

## Kasus
Program ini dirancang untuk memproses data nilai mahasiswa yang mencakup fungsi perhitungan rata-rata nilai, penentuan status kelulusan berdasarkan batas nilai tertentu, serta pencarian nilai tertinggi dari sekumpulan data[cite: 9, 10].

## Test Case

| ID | Target | Input | Expected | Actual Awal | Status Akhir (Retest) |
|---|---|---|---|---|---|
| T1 | rata-rata | `[80, 60, 90, 70]` | `75.0` | `60.0` (Salah karena pembagi statis 5) | PASS |
| T2 | rata-rata | `[100, 80]` | `90.0` | `36.0` (Salah) | PASS |
| T3 | status | `60` | `Lulus` | `Tidak lulus` (Bug batas operator `>`) | PASS |
| T4 | status | `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | tertinggi | `[80, 60, 90, 70]` | `90` | `0` (Bug logika inisialisasi & operator `<`) | PASS |

## Bug Report

1. **Bug ID: B01 (Fungsi `hitung_rata_rata`)**
   - **Gejala:** Hasil rata-rata salah ketika panjang list data tidak sama dengan 5[cite: 9, 10].
   - **Lokasi:** Fungsi `hitung_rata_rata`, baris return `sum(nilai) / 5`[cite: 9, 10].
   - **Akar Penyebab:** Program menggunakan pembagi angka tetap (`5`) alih-alih menggunakan jumlah elemen list aktual (`len(nilai)`)[cite: 9, 14].
   - **Perbaikan:** Mengubah kode menjadi `return sum(nilai) / len(nilai)` serta menambahkan validasi list kosong[cite: 14].

2. **Bug ID: B02 (Fungsi `status`)**
   - **Gejala:** Nilai tepat `60` menghasilkan status "Tidak lulus"[cite: 7, 8, 10].
   - **Lokasi:** Fungsi `status`, baris kondisi `if nilai > 60:`[cite: 8, 10].
   - **Ahkar Penyebab:** Kesalahan operator pembanding (`>` seharusnya `>=`) pada nilai batas kelulusan[cite: 7, 8].
   - **Perbaikan:** Mengubah operator menjadi `if nilai >= 60:`[cite: 8, 14].

3. **Bug ID: B03 (Fungsi `nilai_tertinggi`)**
   - **Gejala:** Fungsi selalu mengembalikan angka `0`[cite: 10].
   - **Lokasi:** Fungsi `nilai_tertinggi`[cite: 9, 10].
   - **Akar Penyebab:** Variabel `tertinggi` diinisialisasi dengan `0` dan arah operator perbandingan salah (`x < tertinggi`)[cite: 9, 10].
   - **Perbaikan:** Menginisialisasi `tertinggi` dengan elemen pertama list (`nilai[0]`) dan mengubah operator menjadi `x > tertinggi`[cite: 14].

## Retest
Setelah dilakukan perbaikan kode dengan perubahan minimal dan terarah, seluruh pengujian dijalankan kembali dan menghasilkan status **PASS** tanpa adanya regresi pada test case lainnya[cite: 8, 10, 13, 14].

## Cara Menjalankan
Jalankan perintah berikut melalui terminal di root folder proyek[cite: 10, 11]:
```bash
python3 praktik/praktik_4_debugging.py