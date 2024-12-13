class DividirView:
    def obtener_numeros(self):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError: #si los datos ingresados no son numeros pide que se ingresen otra vez
            print("Error: Por favor, ingrese números válidos.")
            return self.obtener_numeros()

    def mostrar_resultado(self, num1, num2, operador, resultado):
        print(f"El resultado de {num1} {operador} {num2} es: {resultado}")

    def mostrar_error(self, error):
        print(f"Error: {error}")
