from fastapi import HTTPException
import psycopg2
import os

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            database=os.environ.get("DB_NAME"),
        )
        # Inicializa el cursor correctamente
        self.cursor = self.connection.cursor()
        
    def insertar_publicacion(self, id_usuario, texto):
        self.cursor.execute("SELECT insertar_publicacion(%s,%s)", (id_usuario, texto))
        self.connection.commit()
        return self.cursor.fetchone()[0]
        
    def close(self):
        # Cierra la conexión a la base de datos.
        self.cursor.close()
        self.connection.close()
