""" menu del programa """
import os
import helpers
import manager

def loop():
    out_var = True

    switch = {
        "1": "Listando los clientes...\n",
        "2": "Mostrando un cliente...\n",
        "3": "Añadiendo un cliente...\n",
        "4": "Modificando un cliente...\n",
        "5": "Borrando un cliente...\n",
        "6": "Saliendo...\n",
    }

    def listar(x):
        print(switch.get(x))
        manager.show_all()

    def show(x):
        print(switch.get(x))
        manager.find()

    def add(x):
        print(switch.get(x))
        manager.add()
        print("Cliente añadido correctamente\n")

    def edit(x):
        print(switch.get(x))

    def delete(x):
        print(switch.get(x))

    def out(x):
        print(switch.get(x))
        nonlocal out_var
        out_var = False

    switch_func = {
        '1': listar,
        '2': show,
        '3': add,
        '4': edit,
        '5': delete,
        '6': out,
    }

    while out_var:
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
        func = switch_func.get(option)
        func(option)
        input("\nPresiona ENTER para continuar...")
