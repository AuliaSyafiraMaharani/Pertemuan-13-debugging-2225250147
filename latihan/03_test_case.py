# Latihan 3: Bug Batas Kelulusan[cite: 8]
def status_lulus(nilai):
    if nilai > 60:  # Bug operator batas
        return "Lulus"
    return "Tidak lulus"

if __name__ == "__main__":
    # Rancang test case untuk 59, 60, dan 61
    for n in [59, 60, 61]:
        print(f"Nilai {n}: {status_lulus(n)}")