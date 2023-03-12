# Exception handing in python 
import MySQLdb as ms

conn = ms.connect(host='localhost', user='root', password='root', database='maha')
cursor = conn.cursor()

try:
    rows = cursor.execute('select * from students')

except ms.Error as e:    # For Handling errors related to MYSQLDB
    print(e)

except:
    print('Unknown error occured')  # For Handling exception 
