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

    # Guardar en la tabla historial
    def guardar_operacion(self, num1, num2, operador, resultado):
        operacion = f"{num1} {operador} {num2}"
        query = "INSERT INTO historial (operacion, resultado) VALUES (%s, %s)"
        valores = (operacion, resultado)
        self.cursor.execute(query, valores)
        self.db.commit()
        print("Operación guardada en el historial.")

    # Mostrar las operaciones guardadas en historial
    def mostrar_operaciones(self):
        query = "SELECT * FROM historial"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        
        if resultados:
            print("Historial de operaciones:")
            for operacion in resultados:
                print(f"{operacion[0]} | {operacion[1]} = {operacion[2]}")
        else:
            print("No hay operaciones registradas en el historial.")
