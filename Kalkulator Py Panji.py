def penjumlahan():
    """Fungsi untuk penjumlahan dua angka"""
    print("\n--- Penjumlahan ---")
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 + angka2
        print(f"Hasil penjumlahan: {angka1} + {angka2} = {hasil}")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

def keliling_luas():
    """Fungsi untuk menghitung keliling dan luas persegi panjang"""
    print("\n--- Keliling dan Luas Persegi Panjang ---")
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        if panjang < 0 or lebar < 0:
            print("Panjang dan lebar tidak boleh negatif!")
            return
        keliling = 2 * (panjang + lebar)
        luas = panjang * lebar
        print(f"Keliling persegi panjang: {keliling:.2f}")
        print(f"Luas persegi panjang: {luas:.2f}")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

def cek_usia():
    """Fungsi untuk cek usia"""
    print("\n--- Cek Usia ---")
    try:
        usia = int(input("Masukkan usia Anda: "))
        if usia >= 18:
            print("Anda sudah dewasa!")
        elif usia >= 13:
            print("Anda remaja.")
        else:
            print("Anda masih anak-anak.")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.")

def main():
    """Fungsi utama untuk menu"""
    while True:
        print("\n=== PROGRAM SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Keliling dan Luas Persegi Panjang")  # Diperbarui label menu
        print("3. Cek Usia")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == '1':
            penjumlahan()
        elif pilihan == '2':
            keliling_luas()
        elif pilihan == '3':
            cek_usia()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-4.")

# Jalankan program
if __name__ == "__main__":
    main()
