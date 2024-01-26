import bcrypt
import csv
import os
import regex as re
from Cliente import Cliente
from Crucero import Crucero
from Reserva import Reserva

if __name__ == "__main__":
    clientes: list[Cliente] = []
    cruceros: list[Crucero] = []
    reservas: list[Reserva] = []
    while True:
        print("Ingrese una opcion")
        print("1. Registrar cliente")
        print("2. Registrar crucero")
        print("3. Registrar reserva")
        print("4. Listar clientes")
        print("5. Listar cruceros")
        print("6. Listar reservas")
        print("7. Salir")
        opcion = int(input("--> "))
        if opcion == 1:
            email = input("Ingrese email: ")
            if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                print("El email no es valido")
            else:
                nombre_apellido = input("Ingrese nombre y apellido: ")
                contrasena = input("Ingrese contraseña: ").encode()
                contrasena = bcrypt.hashpw(contrasena, bcrypt.gensalt()).decode()
                cliente = Cliente(email, nombre_apellido, contrasena)
                clientes.append(cliente)
                print("Cliente registrado")
        elif opcion == 2:
            nombre = input("Ingrese nombre: ")
            destino = input("Ingrese destino: ")
            precio = float(input("Ingrese precio: "))
            crucero = Crucero(nombre, destino, precio)
            cruceros.append(crucero)
            print("Crucero registrado")
        elif opcion == 3:
            email = input("Ingrese email: ")
            nombre_crucero = input("Ingrese el nombre del crucero: ")
            if not any(cliente.email == email for cliente in clientes):
                print("El email no existe")
            elif not any(crucero.nombre == nombre_crucero for crucero in cruceros):
                print("El crucero no existe")
            else:
                reserva = Reserva(email, nombre_crucero)
                reservas.append(reserva)
                print("Reserva registrada")
        elif opcion == 4:
            for cliente in clientes:
                print(cliente)
        elif opcion == 5:
            for crucero in cruceros:
                print(crucero)
        elif opcion == 6:
            for reserva in reservas:
                print(reserva)
        elif opcion == 7:
            archivo = open("clientes.csv", "w", newline='')
            writer = csv.writer(archivo)
            for cliente in clientes:
                writer.writerow([cliente.email, cliente.nombre_apellido, cliente.contrasena])
            archivo.close()
            archivo = open("cruceros.csv", "w", newline='')
            writer = csv.writer(archivo)
            for crucero in cruceros:
                writer.writerow([crucero.nombre, crucero.destino, crucero.precio])
            archivo.close()
            archivo = open("reservas.csv", "w", newline='')
            writer = csv.writer(archivo)
            for reserva in reservas:
                writer.writerow([reserva.email, reserva.nombre_crucero])
            archivo.close()
            print("Adios")
            break
        else:
            print("Opcion invalida")
        input("Presione enter para continuar")
        os.system("cls")