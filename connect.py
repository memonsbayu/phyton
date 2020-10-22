import mysql.connector
def koneksi():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="sewa_alat_olahraga",
        autocommit=True
    )
    if db.is_connected():
        return db
    else:
        print ('DB disconnected!')
    
 
