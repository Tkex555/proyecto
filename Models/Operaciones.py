# Models/OperacionBase.py

import mysql.connector

class OperacionBase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",     
            user="root",    
            password="",  
            database="calculadora"
        )
        self.cursor = self.db.cursor()

    def guardar_operacion(self, num1, num2, operador, resultado):
        query = "INSERT INTO operaciones (num1, num2, operador, resultado) VALUES (%s, %s, %s, %s)"
        valores = (num1, num2, operador, resultado)
        self.cursor.execute(query, valores)
        self.db.commit()
