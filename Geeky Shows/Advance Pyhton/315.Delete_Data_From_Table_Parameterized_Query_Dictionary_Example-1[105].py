# Delete Row - Dictionary
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='Seth7706',
        host='localhost',
        database='pdb',
        port=3306
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable To Connect')
sql='DELETE FROM student WHERE stuid=%(id)s'
myc=conn.cursor()
del_value={'id':10}
try:
    myc.execute(sql,del_value)
    conn.commit()   # Commiting The Changes
    print(myc.rowcount,'Row Deleted')
except:
    conn.rollback() # Rollback The Changes
    print('Unable To Delete Data')
myc.close() # Close Cursor
conn.close()    # Close Connection