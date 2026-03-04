Dokumentasi Algoritma Diffie-Hellman Key Exchange

Repositori ini berisi implementasi sederhana dari protokol pertukaran kunci Diffie-Hellman menggunakan bahasa pemrograman Python. Kode ini dirancang untuk mensimulasikan bagaimana dua pihak dapat menghasilkan kunci rahasia yang sama melalui saluran komunikasi publik.

### Langkah-Langkah Eksekusi Kode

Program ini menjalankan urutan logika sebagai berikut:

1.  **Inisialisasi Fungsi Eksponensial Modular**: Program mendefinisikan fungsi `power_mod` yang menggunakan algoritma *Square and Multiply* untuk menghitung nilai pangkat besar secara efisien dalam sistem modulus.
2.  **Penetapan Parameter Publik**: Program menggunakan parameter yang disepakati bersama, yaitu bilangan prima (p = 23) dan generator (g = 5).
3.  **Input Kunci Privat**: Pengguna diminta untuk memasukkan kunci privat Alice ($x$) dan kunci privat Bob (y) secara manual melalui terminal.
4.  **Perhitungan Kunci Publik**:
    * Program menghitung kunci publik Alice (A) dengan rumus g^x (mod p).
    * Program menghitung kunci publik Bob (B) dengan rumus g^y (mod p).
5.  **Simulasi Pertukaran Kunci**: Program menampilkan kunci publik A dan B yang seolah-olah dikirimkan melalui jaringan terbuka.
6.  **Perhitungan Kunci Rahasia Bersama (Shared Secret)**:
    * Alice menerima kunci publik Bob (B) dan menghitung rahasia bersama menggunakan kunci privatnya: S = B^x (mod p).
    * Bob menerima kunci publik Alice (A) dan menghitung rahasia bersama menggunakan kunci privatnya: S = A^y (mod p).
7.  **Verifikasi Akhir**: Program membandingkan hasil perhitungan dari kedua belah pihak. Jika nilainya sama, maka pertukaran kunci dinyatakan berhasil.

## Cara Menjalankan Program

### Prasyarat
Pastikan Anda telah menginstal Python di perangkat Anda.

### Instruksi Menjalankan
1.  Buka terminal atau command prompt.
2.  Navigasikan ke direktori tempat file `diffle-hellman.py` disimpan.
3.  Jalankan perintah berikut:
    ```bash
    python diffle-hellman.py
    ```
4.  Masukkan nilai angka bulat saat diminta untuk kunci privat Alice dan Bob.
5.  Lihat hasil perhitungan kunci publik dan verifikasi shared secret di layar terminal.
