import mysql.connector
from decouple import config

# Creamos el objeto de acceso a los datos
class DAO():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = config('MYSQL_HOST'),
                port = config('MYSQL_PORT'),
                user = config('MYSQL_USER'),
                password = config('MYSQL_PASSWORD'),
                database = config('MYSQL_DB')
            )
        except Exception as e:
            print(e)