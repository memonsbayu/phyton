import pelanggan
import sewa

print('DATA PENYEWAAN PS PEEKABOO.CO')
print('1.Pelanggan')
print('2.Penyewaan')
menu = int(input('Pilih Menu:'))

if(menu==1):
    print("SELAMAT DATANG DI MENU PELANGGAN!")
    print('1.Tambah Data Pelanggan')
    print('2.Ubah Data Pelanggan')
    print('3.Hapus Data Pelanggan')
    print('4.Cari Data Pelanggan')
    print('5.Tampilkan Data Pelanggan')
    menu11 = int(input('Pilih:'))

    if(menu11==1):
        id_pelanggan=input('ID Pelanggan:')
        nama=input('Nama:')
        alamat=input('Alamat: ')
        no_hp=input('No HP:')
        data=[id_pelanggan,nama,alamat,no_hp]
        pelanggan.add(data)
    elif(menu11==2):
        id_pelanggan=input('ID Pelanggan:')
        nama=input('Nama:')
        alamat=input('Alamat: ')
        no_hp=input('No HP:')
        data=[id_pelanggan,nama,alamat,no_hp]
        pelanggan.edit(data)
    elif(menu11==3):
        id_pelanggan=input('ID Pelanggan:')
        data=[id_pelanggan]
        pelanggan.search(data)
        confirm=input('Yakin menghapus data penyewaan ini? [Y/N]:')
        if(confirm=='Y'):
            pelanggan.delete(data)
        else:
            print('Tidak jadi menghapus data penyewaan!')
    elif (menu11==4):
        id_pelanggan=input('ID Pelanggan:')
        data=[id_pelanggan]
        pelanggan.search(data)
    elif(menu11==5):
        pelanggan.show()
    else:
        print('Menu Tidak Tersedia')

if(menu==2):
    print("SELAMAT DATANG DI MENU PENYEWAAN!")
    print('1.Tambah Data Penyewaan')
    print('2.Ubah Data Penyewaan')
    print('3.Hapus Data Penyewaan')
    print('4.Cari Data Penyewaan')
    print('5.Tampilkan Data Penyewaan')
    menu22 = int(input('Pilih:'))

    if(menu22==1):
        id_pelanggan=input('ID Pelanggan:')
        print('1.PS1')
        print('2.PS2')
        print('3.PS3')
        print('4.PS4')
        un=int(input('Unit:'))
        if (un==1):
           unit=('PS1')
        elif (un==2):
           unit=('PS2')
        elif (un==3):
           unit=('PS3')
        elif (un==4):
           unit=('PS4')
        else :
           unit=('Tidak Tersedia!')
        print("Masukan nama unit yang dipilih pada kolom biaya/hari!")
        by=input('Biaya/hari: ')
        if (by=='PS1' or by=='ps1'):
           biaya=('Rp40.000,-')
        elif (by=='PS2' or by=='ps2'):
           biaya=('Rp45.000,-')
        elif (by=='PS3' or by=='ps3'):
           biaya=('Rp50.000,-')
        elif (by=='PS4' or by=='ps4'):
           biaya=('Rp55.000,-')
        else :
           biaya=('Tidak Tersedia!')
        pengambilan=input('Pengambilan:')
        pengembalian=input('Pengembalian:')
        total=input('Total Biaya:')
        data=[is_pelanggan,unit,biaya,pengambilan,pengembalian,total]
        sewa.add(data)
    elif(menu22==2):
        id_pelanggan=input('ID Pelanggan:')
        print('1.PS1')
        print('2.PS2')
        print('3.PS3')
        print('4.PS4')
        un=int(input('Unit:'))
        if (un==1):
           unit=('PS1')
        elif (un==2):
           unit=('PS2')
        elif (un==3):
           unit=('PS3')
        elif (un==4):
           unit=('PS4')
        else :
           unit=('Tidak Tersedia!')
        print("Masukan nama unit yang dipilih pada kolom biaya/hari!")
        by=input('Biaya/hari: ')
        if (by=='PS1' or by=='ps1'):
           biaya=('Rp40.000,-')
        elif (by=='PS2' or by=='ps2'):
           biaya=('Rp45.000,-')
        elif (by=='PS3' or by=='ps3'):
           biaya=('Rp50.000,-')
        elif (by=='PS4' or by=='ps4'):
           biaya=('Rp55.000,-')
        else :
           biaya=('Tidak Tersedia!')
        pengambilan=input('Pengambilan:')
        pengembalian=input('Pengembalian:')
        total=input('Total Biaya:')
        data=[is_pelanggan,unit,biaya,pengambilan,pengembalian,total]
        sewa.edit(data)
    elif(menu22==3):
        id_pelanggan=input('ID Pelanggan:')
        data=[id_pelanggan]
        sewa.search(data)
        confirm=input('Yakin menghapus data pelanggan ini? [Y/N]:')
        if(confirm=='Y'):
            sewa.delete(data)
        else:
            print('Tidak jadi menghapus data pelanggan!')
    elif (menu22==4):
        id_pelanggan=input('ID Pelanggan:')
        data=[id_pelanggan]
        sewa.search(data)
    elif(menu22==5):
        sewa.show()
    else:
        print('Menu Tidak Tersedia')
