import mysql.connector

class ConexionDB:
    def __init__(self): #conexion con la base de datos
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "calculadora"
        }
        self.conexion = mysql.connector.connect(**self.config)
        self.cursor = self.conexion.cursor()

    def obtener_conexion(self):
        return self.conexion
