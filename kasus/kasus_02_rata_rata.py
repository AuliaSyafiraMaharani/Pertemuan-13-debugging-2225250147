# Kasus 2: Rata-Rata Nilai (Bermasalah)
# Program memberikan hasil salah atau error jika jumlah elemen list tidak sesuai dengan pembagi statis[cite: 5, 8, 9].

def rata_rata(data):
    total = sum(data)
    return total / 5  # Bug: Pembagi dipatok angka 5, tidak dinamis

if __name__ == "__main__":
    print("Rata-rata [80, 90, 70]:", rata_rata([80, 90, 70]))