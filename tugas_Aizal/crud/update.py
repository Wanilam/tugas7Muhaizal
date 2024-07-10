
import mysql.connector

def update_record(id,  nama, penulis ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE buku SET id = %s, nama = %s, penulis = %s WHERE id = %s"
        val = (id, nama, penulis, id)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


