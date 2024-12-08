# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:03:56 2024

@author: Dewi
"""

# Program untuk menghitung harga tiket di Kebun Binatang Trisakti

def hitung_harga(umur):
    # Menentukan harga tiket berdasarkan umur
    if umur <= 2:
        return 0  # Gratis untuk umur 2 tahun ke bawah
    elif umur <= 12:
        return 14  # Harga untuk anak-anak (3-12 tahun)
    elif umur <= 64:
        return 23  # Harga untuk dewasa (13-64 tahun)
    else:
        return 18  # Harga untuk lansia (65 tahun ke atas)

def main():
    print("=====SELAMAT DATANG DI KEBUN BINATANG TRISAKTI=====")
    running_total = 0  # Menyimpan total harga tiket
    
    while True:
        # Meminta input umur dari pengguna
        umur = int(input("masukkan umur: "))
        if umur == -1:
            break  # Menghentikan program jika input -1
        
        # Menghitung harga tiket berdasarkan umur
        harga = hitung_harga(umur)
        
        # Menampilkan harga tiket untuk pengunjung saat ini
        if harga == 0:
            print("Gratis")
        else:
            print(f"Harga: ${harga}")
        
        # Menambahkan harga tiket ke total
        running_total += harga
        print(f"Running total: ${running_total:.2f}")
    
    # Meminta input uang dari pengguna
    jumlah_uang = float(input("masukkan jumlah uang: "))
    kembalian = jumlah_uang - running_total
    
    # Menampilkan kembalian
    print(f"Running Kembalian: ${kembalian:.2f}")
    print("=====TERIMAKASIH=====")

# Memanggil fungsi utama
main()