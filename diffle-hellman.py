# Program Pertukaran Kunci Diffie-Hellman Manual

def power_mod(base, exponent, modulus):
    """
    Fungsi manual untuk menghitung (base^exponent) % modulus
    Menggunakan algoritma Square and Multiply
    """
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def main():
    print("=== Simulasi Pertukaran Kunci Diffie-Hellman ===\n")

    # 1. Parameter Publik (Disepakati bersama)
    p = 23  
    g = 5
    print(f"Parameter Publik yang disepakati:\nPrima (p): {p}\nGenerator (g): {g}\n")

    # 2. Input Kunci Privat dari User
    try:
        x = int(input("Masukkan kunci privat Alice (x): "))
        y = int(input("Masukkan kunci privat Bob (y): "))
        print("")
    except ValueError:
        print("Error: Harap masukkan angka bulat (integer) saja!")
        return

    # 3. Menghitung Kunci Publik (A dan B)
    # Rumus: A = g^x mod p
    alice_public = power_mod(g, x, p)
    # Rumus: B = g^y mod p
    bob_public = power_mod(g, y, p)

    print(f"--- Proses Pertukaran Kunci ---")
    print(f"Alice menghitung kunci publik A dan mengirimnya ke jaringan: {alice_public}")
    print(f"Bob menghitung kunci publik B dan mengirimnya ke jaringan: {bob_public}\n")

    # 4. Menghitung Shared Secret (S)
    # Alice menerima B, lalu menghitung S = B^x mod p
    alice_shared_secret = power_mod(bob_public, x, p)
    
    # Bob menerima A, lalu menghitung S = A^y mod p
    bob_shared_secret = power_mod(alice_public, y, p)

    # 5. Verifikasi Akhir
    print("=== Hasil Shared Secret ===")
    print(f"Shared Secret di sisi Alice: {alice_shared_secret}")
    print(f"Shared Secret di sisi Bob: {bob_shared_secret}")

    if alice_shared_secret == bob_shared_secret:
        print("\nBERHASIL: Kalian berdua memiliki kunci rahasia yang sama tanpa mengirim kunci x atau y!")
    else:
        print("\nGAGAL: Kunci tidak cocok (pastikan input benar).")

if __name__ == "__main__":
    main()