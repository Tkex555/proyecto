from Models.Operaciones import OperacionBase

class Dividir(OperacionBase):
    def calcular(self, num1, num2):
        if num2 == 0: #si el numero ingresado es 0 no permitira continuar
            raise ZeroDivisionError("No se puede dividir por cero.") 
        resultado = num1 / num2
        self.guardar_operacion(num1, num2, "/", resultado) #division
        return resultado
