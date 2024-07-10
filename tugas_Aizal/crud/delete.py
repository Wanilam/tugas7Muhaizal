import mysql.connector

def delete_record(id):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpustakaan"
    )

    mycursor = mysb.cursor()

    sql = "DELETE FROM buku WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record(s) deleted")

    mycursor.close()
    mysb.close()