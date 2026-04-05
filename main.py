# Program untuk menentukan bilangan Ganjil atau Genap
# Tugas Komputasi Dasar

def cek_ganjil_genap():
    try:
        # Input dari pengguna
        angka = int(input("Masukkan sebuah bilangan bulat: "))

        # Logika pengecekan menggunakan operator moduloa
        if angka % 2 == 0:
            print(f"Angka {angka} adalah bilangan GENAP.")
        else:
            print(f"Angka {angka} adalah bilangan GANJIL.")
            
    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.")

# Menjalankan program
cek_ganjil_genap()