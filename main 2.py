import member
import math
print("1. Tambah Member")
print("2. Ubah Member")
print("3. Hapus Member")
print("4. Tampilkan Member")
print("5. Cari Member")
menu2= int (input('[Member] pilih='))
if (menu2==1):
    Nomor_Barang=int(input("Nomor Barang:"))
    Lama_Sewa=int(input("Lama Sewa:"))
    Harga=(10000*Lama_Sewa)
    data=[Nomor_Barang,Lama_Sewa,Harga]
    member.add(data)
elif(menu2==2):
    id_member=input("No Member:")
    Nomor_Barang=input('Nomor_Barang:')
    Lama_Sewa=int(input('Lama_Sewa:'))
    Harga=(10000*Lama_Sewa)
    data=[Nomor_Barang,Lama_Sewa,Harga,id_member]
    member.edit(data)
elif (menu2==3):
    id_member=input('No. member:')
    data=[id_member]
    confirm=input('Yakin menghapus memberini?[y/n]')
    if(confirm=="y"):
        member.delete(data)
    else:
        print('Data batal di hapus')
elif (menu2==4):
    member.show()

elif(menu2==5):
    id_member=input('No.menber:')
    data=[id_member]
    member.search(data)
else:
    print('Menu tidak tersedia')
