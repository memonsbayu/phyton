import mysql.connector
import connect
db=connect.koneksi()
#menambahkan data baru ke dalam table member

def add(data):
    cursor=db.cursor()
    sql="""INSERT INTO member(nama,alamat)VALUES(%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil ditambhkan!'.format(cursor.rowcount))

    #menampilkan seluruh data dari tabel member

def show():
    cursor=db.cursor()
    sql="""SELECT*FROM member"""
    cursor.execute(sql)

    result=cursor.fetchall()
    print("--------------------------------------")
    print("|ID |NAMA \t\t|ALAMAT\t\t|")
    print("--------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|")



#mengubah data per record berdasarkan id pada table member

def edit(data):
    cursor=db.cursor()
    sql="""UPDATE member SET nama=%s,alamat=%sWHERE id=%s"""

    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil diubah!'.format(cursor.rowcount))


#menghapus data dari tabel member

def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM member WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil dihapus!'.format(cursor.rowcount))


#mencari data dari tabel member

def search(id_member):
    cursor=db.cursor()
    sql="""SELECT*FROM member WHERE id=%s"""
    cursor.execute(sql,id_member)

    result=cursor.fetchall()
    print("--------------------------------------")
    print("|ID |NAMA \t|ALAMAT\t\t|")
    print("--------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|")
        print("--------------------------------------")



    
