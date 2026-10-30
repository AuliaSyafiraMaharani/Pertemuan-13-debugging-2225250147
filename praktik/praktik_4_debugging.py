# Nama File: praktik/praktik_4_debugging.py
# Deskripsi: Program perbaikan bug untuk perhitungan rata-rata, status kelulusan, dan nilai tertinggi.

def hitung_rata_rata(nilai):
    # Perbaikan: Menghindari pembagian dengan 0 dan menyesuaikan pembagi dengan jumlah elemen list[cite: 14]
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status(nilai):
    # Perbaikan: Mengubah operator dari '>' menjadi '>=' agar nilai 60 terbaca Lulus (batas lulus)[cite: 7, 8, 14]
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    # Perbaikan: Menangani list kosong dan memperbaiki logika perbandingan elemen list[cite: 9, 14]
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

# Pengujian Program (Test Case Utama)
if __name__ == "__main__":
    nilai = [80, 60, 90, 70]
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(nilai))