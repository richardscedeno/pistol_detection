import mysql.connector
from decouple import config

conn = mysql.connector.connect(
    user = config('MYSQL_USER'),
    password = config('MYSQL_PASSWORD'),
    host = config('MYSQL_HOST'),
    database = config('MYSQL_DB'),
    port = config('MYSQL_PORT')
)

print(conn)