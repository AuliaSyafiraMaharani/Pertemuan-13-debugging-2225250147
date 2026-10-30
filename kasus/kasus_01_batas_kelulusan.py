# Kasus 1: Batas Kelulusan (Bermasalah)
# Program berjalan tanpa SyntaxError, tetapi memiliki logical bug pada nilai batas 60[cite: 4, 5, 8].

def status_lulus(nilai):
    # Bug: Menggunakan operator '>' sehingga nilai tepat 60 dianggap tidak lulus
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

if __name__ == "__main__":
    print("Nilai 75:", status_lulus(75))
    print("Nilai 60:", status_lulus(60))  # Expected: Lulus, Actual: Tidak lulus (Bug!)
    print("Nilai 59:", status_lulus(59))