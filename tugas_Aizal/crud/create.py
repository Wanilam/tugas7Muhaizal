import mysql.connector

def create_record(id, nama, penulis):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpustakaan"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO buku (id, nama, penulis) VALUES ( %s, %s, %s)"
    val = (id, nama, penulis)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()