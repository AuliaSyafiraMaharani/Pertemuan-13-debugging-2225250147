# Latihan 4: Debug Breakpoint Simulation[cite: 4]
def hitung_faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

if __name__ == "__main__":
    # Gunakan breakpoint pada VS Code di baris pemanggilan fungsi ini
    print("Faktorial 5 adalah:", hitung_faktorial(5))