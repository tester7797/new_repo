import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Krishnan9979',
    database='mydb',
    port='3306'
)

my_curser=conn.cursor()
my_curser.execute('show tables')

get_data=my_curser.fetchall()

print(get_data)

conn.close()