# Latihan 2: Menelusuri Fungsi[cite: 8]
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

if __name__ == "__main__":
    print("Total setelah diskon:", hitung_diskon(200000, 10))