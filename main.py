# main.py

from Controllers.SumarController import SumarController
from Controllers.RestarController import RestarController
from Controllers.MultiplicarController import MultiplicarController
from Controllers.DividirController import DividirController

def main():
    while True:
        print("\nElige una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            controller = SumarController()
            controller.realizar_suma()
        elif opcion == "2":
            controller = RestarController()
            controller.realizar_resta()
        elif opcion == "3":
            controller = MultiplicarController()
            controller.realizar_multiplicacion()
        elif opcion == "4":
            controller = DividirController()
            controller.realizar_division()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
