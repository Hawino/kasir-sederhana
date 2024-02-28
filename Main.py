# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LNXgya2Fvw0wPwizRj8LgW3D2Ezh3DHK
"""

#Library untuk menginstal module pembuat Tabel
!pip install tabulate
from tabulate import tabulate

class Transaction():
  """
  Class untuk mensimulasikan transaksi pembelian.

  Atribut:
    nama_item: List yang berisi nama item yang dibeli.
    jumlah_item: List yang berisi jumlah item yang dibeli.
    harga_item: List yang berisi harga item yang dibeli.
  """
  def __init__(self):
    self.nama_item =[]
    self.jumlah_item =[]
    self.harga_item =[]
    self.total_harga =[]


  def add_item(self,nama,jumlah,harga):
    """
  Menambahkan item baru ke transaksi.

  Args:
    nama: Nama item yang ingin ditambahkan.
    jumlah: Jumlah item yang ingin ditambahkan.
    harga: Harga item yang ingin ditambahkan.

  Returns:
    List barang belanja yang sudah diinput.
    """
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai
    try: #Memberi info jika input "Jumlah Item" yang tidak sesuai
      int(jumlah)
    except ValueError:
      print("Jumlah Item yang dimasukan harus Angka")
      return None
    try: #Memberi info jika input "Harga Item" yang tidak sesuai
      int(harga)
    except ValueError:
      print("Harga Item yang dimasukan harus Angka")
      return None

    self.nama_item.append(nama_kecil) #Memasukan data input ke list
    self.jumlah_item.append(jumlah)
    self.harga_item.append(harga)

    self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item)) #Menggabungkan list nama, jumlah & harga
    print(f'Item yang dibeli: {self.semua_order}')


  def update_nama_item(self,nama,update_nama):
    """
  Mengubah nama item yang sudah ada.

  Args:
    nama: Nama item yang ingin diubah.
    update_nama: Nama baru untuk item.

  Returns:
    List barang belanja yang sudah diupdate itemnya.
    """
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai
    update_kecil = str(update_nama.lower())

    for i in range(len(self.nama_item)): #Program mengganti "Nama Item"
      if self.nama_item[i] == nama_kecil:
        self.nama_item[i] = update_kecil
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Item yang dibeli: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Item '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        return None


  def update_jumlah_item(self,nama,jumlah_baru):
    """
  Mengubah jumlah item yang sudah ada.

  Args:
    nama_item: Nama item yang ingin diubah jumlahnya.
    jumlah_baru: Jumlah baru untuk item.

  Returns:
    List barang belanja yang sudah diupdate jumlahnya.
    """
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai
    try: #Code untuk memberi info input "Jumlah Item" yang tidak sesuai
      int(jumlah_baru)
    except ValueError:
      print("Jumlah Item Baru yang dimasukan harus Angka")
      return None

    for i in range(len(self.nama_item)): #Program mengganti "Jumlah Item"
      if self.nama_item[i] == nama_kecil:
        self.jumlah_item[i] = jumlah_baru
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Item yang dibeli: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Item '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        return None


  def update_harga_item(self,nama,harga_baru):
    """
  Mengubah harga item yang sudah ada.

  Args:
    nama_item: Nama item yang ingin diubah harganya.
    harga_baru: Harga baru untuk item.

  Returns:
    List barang belanja yang sudah diupdate harganya.
    """
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai
    try: #Code untuk memberi info input "Harga Item" yang tidak sesuai
      int(harga_baru)
    except ValueError:
      print("Harga Item Baru yang dimasukan harus Angka")
      return None

    for i in range(len(self.nama_item)): #Program mengganti "Harga Item"
      if self.nama_item[i] == nama_kecil:
        self.harga_item[i] = harga_baru
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Item yang dibeli: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Item '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        return None


  def delete_item(self,nama):
    """
  Menghapus item dari transaksi.

  Args:
    nama_item: Nama item yang ingin dihapus.

  Returns:
    List barang belanja setelah ada item yang dihapus.
    """
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai

    for i in range(len(self.nama_item)): #Program menghapus "Nama, Jumlah, Harga dari 1 Item"
      if self.nama_item[i] == nama_kecil:
        self.nama_item.pop(i)
        self.jumlah_item.pop(i)
        self.harga_item.pop(i)
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Item yang dibeli: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Item '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        return None


  def reset_transaction(self):
    """
  Menghapus semua item dari transaksi.

  Args:
    None.

  Returns:
    None
    """
    self.nama_item.clear() #Program menghapus semua Item
    self.jumlah_item.clear()
    self.harga_item.clear()
    print('Semua Item Berhasil Didelete')


  def check_order(self):
    """
  Melihat semua item dari transaksi dalam bentuk tabel.

  Args:
    None.

  Returns:
    Tabel list semua barang belanjaan, jumlah barang, harga/unit, total biaya/unit
    """
    self.total_harga = [x * y for x, y in zip(self.jumlah_item, self.harga_item)] #Membuat variabel tambahan, Total Harga/Satuan
    self.semua_order=list(zip(self.nama_item, self.jumlah_item, #Menggabungkan semua List "Nama Item","Jumlah Item","Harga Satuan","Total Harga"
                              self.harga_item, self.total_harga))
    print(tabulate(self.semua_order,headers=["Nama Item","Jumlah Item","Harga Satuan","Total Harga"])) #Membuat Tabel


  def total_price(self):
    """
  Menghitung Total Harga list barang belanjaan.

  Args:
    None.

  Returns:
    Total harga dan list barang belanjaan.
    """
    total = 0 #Menghitung seluruh Total Harga
    for i in range(len(self.jumlah_item)):
      total += ((self.jumlah_item[i])*(self.harga_item[i]))

    self.semua_order = list(zip(self.nama_item, self.jumlah_item, self.harga_item)) #Menggabungkan semua List "Nama Item","Jumlah Item","Harga Satuan"
    print(f'Item yang dibeli: {self.semua_order}')

    if 0 <= total < 200_000: #Menentukan Diskon yang didapatkan dan Total Harga Akhir
      print(f'Total belanjaan Anda: Rp{total}')
    elif 200_000 <= total < 300_000:
      diskon = 0.05
      total_akhir = total - (total*diskon)
      print(f'Total belanjaan Anda: Rp{total_akhir} setelah mendapatkan Diskon ({diskon*100}%): Rp{total*diskon}')
    elif 300_000 <= total < 500_000:
      diskon = 0.08
      total_akhir = total - (total*diskon)
      print(f'Total belanjaan Anda: Rp{total_akhir} setelah mendapatkan Diskon ({diskon*100}%): Rp{total*diskon}')
    elif total > 500_000:
      diskon = 0.1
      total_akhir = total - (total*diskon)
      print(f'Total belanjaan Anda: Rp{total_akhir} setelah mendapatkan Diskon ({diskon*100}%): Rp{total*diskon}')