""" menu del programa """
import os
import helpers


def loop():
    while True:
        helpers.clear()

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")
        helpers.clear()
        switch = {
            "1": "Listando los clientes...\n",
            "2": "Mostrando un cliente...\n",
            "3": "Añadiendo un cliente...\n",
            "4": "Modificando un cliente...\n",
            "5": "Borrando un cliente...\n",
            "6": "Saliendo...\n",
        }
        print(switch.get(option))
        if option == '6':
            break
        input("\nPresiona ENTER para continuar...")
