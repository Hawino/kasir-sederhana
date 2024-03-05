#Library untuk menginstal module pembuat Tabel
pip install tabulate
from tabulate import tabulate
#Library untuk menginstal module pembuat Tabel di Google
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

  def add_item(self):
    """
  Menambahkan item baru ke transaksi.

  Args:
    nama: Nama item yang ingin ditambahkan.
    jumlah: Jumlah item yang ingin ditambahkan.
    harga: Harga item yang ingin ditambahkan.

  Returns:
    List barang belanja yang sudah diinput.
    """
    print("-"*60)
    print("Masukkan Nama, Jumlah & Harga Barang")
    print("-"*60)

    nama = input("Input Nama Barang: ")
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai

    jumlah = int(input("Input Jumlah Barang : "))
    try: #Memberi info jika input "Jumlah Item" yang tidak sesuai
      int(jumlah)
    except ValueError:
      print("Jumlah Item yang dimasukan harus Angka")
      jumlah = int(input("Input Jumlah Barang : "))

    harga = int(input("Input Harga : "))
    try: #Memberi info jika input "Harga Item" yang tidak sesuai
      int(harga)
    except ValueError:
      print("Harga Item yang dimasukan harus Angka")
      harga = int(input("Input Harga : "))

    self.nama_item.append(nama_kecil) #Memasukan data input ke list
    self.jumlah_item.append(jumlah)
    self.harga_item.append(harga)

    self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item)) #Menggabungkan list nama, jumlah & harga
    print(f'Barang di Keranjang saat ini: {self.semua_order}')

    self.menu()


  def update_nama_item(self):
    """
  Mengubah nama item yang sudah ada.

  Args:
    nama: Nama item yang ingin diubah.
    update_nama: Nama baru untuk item.

  Returns:
    List barang belanja yang sudah diupdate itemnya.
    """
    print("-"*60)
    print("Masukkan Nama Barang yang ingin diupdate Namanya")
    print("-"*60)

    nama = input("Input Nama Barang: ")
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai

    update_nama = input("Input Nama Barang yang baru: ")
    update_kecil = str(update_nama.lower())

    for i in range(len(self.nama_item)): #Program mengganti "Nama Item"
      if self.nama_item[i] == nama_kecil:
        self.nama_item[i] = update_kecil
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Barang di Keranjang saat ini: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Barang '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        self.menu()

    self.menu()

  def update_jumlah_item(self):
    """
  Mengubah jumlah item yang sudah ada.

  Args:
    nama_item: Nama item yang ingin diubah jumlahnya.
    jumlah_baru: Jumlah baru untuk item.

  Returns:
    List barang belanja yang sudah diupdate jumlahnya.
    """
    print("-"*60)
    print("Masukkan Nama Barang yang ingin diupdate Jumlahnya")
    print("-"*60)

    nama = input("Input Nama Barang: ")
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai

    jumlah_baru = int(input("Input Jumlah Barang baru: "))
    try: #Code untuk memberi info input "Jumlah Item" yang tidak sesuai
      int(jumlah_baru)
    except ValueError:
      print("Jumlah Barang Baru yang dimasukan harus Angka")
      jumlah_baru = input("Input Jumlah Barang baru: ")

    for i in range(len(self.nama_item)): #Program mengganti "Jumlah Item"
      if self.nama_item[i] == nama_kecil:
        self.jumlah_item[i] = jumlah_baru
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Barang di Keranjang saat ini: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Barang '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        self.menu()

    self.menu()


  def update_harga_item(self):
    """
  Mengubah harga item yang sudah ada.

  Args:
    nama_item: Nama item yang ingin diubah harganya.
    harga_baru: Harga baru untuk item.

  Returns:
    List barang belanja yang sudah diupdate harganya.
    """
    print("-"*60)
    print("Masukkan Nama Barang yang ingin diupdate Harganya")
    print("-"*60)

    nama = input("Input Nama Barang: ")
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai

    harga_baru = int(input("Input Harga Barang baru: "))
    try: #Code untuk memberi info input "Harga Item" yang tidak sesuai
      int(harga_baru)
    except ValueError:
      print("Harga Barang Baru yang dimasukan harus Angka")
      harga_baru = input("Input Harga Barang baru: ")

    for i in range(len(self.nama_item)): #Program mengganti "Harga Item"
      if self.nama_item[i] == nama_kecil:
        self.harga_item[i] = harga_baru
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Barang di Keranjang saat ini: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Barang '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        self.menu()

    self.menu()


  def delete_item(self):
    """
  Menghapus item dari transaksi.

  Args:
    nama_item: Nama item yang ingin dihapus.

  Returns:
    List barang belanja setelah ada item yang dihapus.
    """
    print("-"*60)
    print("Masukkan Nama Barang yang ingin dihapus")
    print("-"*60)

    nama = input("Input Nama Barang: ")
    nama_kecil = str(nama.lower()) #Mencegah format input "Nama Item" yang tidak sesuai

    for i in range(len(self.nama_item)): #Program menghapus "Nama, Jumlah, Harga dari 1 Item"
      if self.nama_item[i] == nama_kecil:
        self.nama_item.pop(i)
        self.jumlah_item.pop(i)
        self.harga_item.pop(i)
        self.semua_order=list(zip(self.nama_item, self.jumlah_item, self.harga_item))
        print(f'Barang di Keranjang saat ini: {self.semua_order}')
      elif not nama_kecil in self.nama_item: #Memberikan info jika "Nama Item" yang diinput salah
        print(f"Barang '{nama_kecil}' tidak ada di transaksi sebelumnya.")
        self.menu()

    self.menu()


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
    print('Semua Barang di keranjang berhasil dihapus')
    self.menu()

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
    print("-"*60)
    print("List semua Barang yang ada di Keranjang Anda")
    print("-"*60)
    print(tabulate(self.semua_order,headers=["Nama Item","Jumlah Item","Harga Satuan","Total Harga"])) #Membuat Tabel

    self.menu()

  def total_price(self):
    """
  Menghitung Total Harga list barang belanjaan.

  Args:
    None.

  Returns:
    Total harga dan list barang belanjaan.
    """
    print("-"*60)
    print("Total Belanja Anda")
    print("-"*60)

    total = 0 #Menghitung seluruh Total Harga
    for i in range(len(self.jumlah_item)):
      total += ((self.jumlah_item[i])*(self.harga_item[i]))

    self.semua_order = list(zip(self.nama_item, self.jumlah_item, self.harga_item)) #Menggabungkan semua List "Nama Item","Jumlah Item","Harga Satuan"
    print(f'Barang yang dibeli: {self.semua_order}')

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

    self.menu()

  def menu(self):
    print()
    print("-"*60)
    print("SELAMAT DATANG DI SELF SERVICE CASHIER PACMANN")
    print("-"*60)
    print("1. Masukkan Barang Belanja ")
    print("2. Update Nama Barang Belanja")
    print("3. Update Jumlah Barang Belanja")
    print("4. Update Harga Barang Belanja ")
    print("5. Menghapus Barang Belanja")
    print("6. Menghapus Semua Barang di Keranjang (RESET)")
    print("7. Check Keranjang Belanja")
    print("8. Total Belanja")
    print("9. Exit\n")

    choice = int(input('Masukkan Nomor Menu : '))

    try:
      if choice == 1:
        self.add_item()
      elif choice == 2:
        self.update_nama_item()
      elif choice == 3:
        self.update_jumlah_item()
      elif choice == 4:
        self.update_harga_item()
      elif choice == 5:
        self.delete_item()
      elif choice == 6:
        self.reset_transaction()
      elif choice == 7:
        self.check_order()
      elif choice == 8:
        self.total_price()
      elif choice == 9:
        print("-"*60)
        print("Terima kasih telah mengunjungi Supermarket Kami.")
        print("-"*60)
        pass
    except ValueError:
      print("Input Anda salah.\n")
      self.menu()

        
start = Transaction()
start.menu()