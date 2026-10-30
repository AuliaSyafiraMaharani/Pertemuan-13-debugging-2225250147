# Kasus 3: File Nilai (Diperbaiki dengan try-except)
def baca_data_nilai(nama_file):
    try:
        # Mencoba membuka dan membaca file
        file = open(nama_file, "r")
        baris = file.readlines()
        file.close()
        return baris
    except FileNotFoundError:
        # Menangani exception jika file tidak ditemukan
        print(f"Peringatan: File '{nama_file}' tidak ditemukan.")
        return []

if __name__ == "__main__":
    # Menjalankan fungsi dengan penanganan error
    baca_data_nilai("data_kosong.txt")