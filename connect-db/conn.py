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

    def save_data(self, data):
        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                query = 'INSERT INTO datos (imagen, descripcion_img, id_tipo) VALUES (%s, %s, %s)'
                values = (data[0], data[1], data[2])
                cursor.execute(query, values)
                self.conn.commit()
                # print('Detección registrada con éxito!')
            except Exception as e:
                print(e)