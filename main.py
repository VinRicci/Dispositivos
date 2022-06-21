from device import Device
from advancedremote import AdvancedRemote
from radio import Radio
from remote import Remote
from tv import Tv
from smarttv import SmartTv


bandera: bool = True
print("Escoge un dispositivo")
print("1. Radio")
print("2. Tv")
print("3. Smart-Tv")
op = int(input("Ingrese opcion: "))
if op == 1:
    dispositivo: Device = Radio()
    print("Escoge un control")
    print("1. Control normal")
    print("2. Control avanzado")
    op2 = int(input("Ingrese opcion: "))
    if op2 == 1:
        control: Remote = Remote(dispositivo)
        while bandera:
            print("Funciones")
            print("1. Encender/Apagar")
            print("2. Subir canal")
            print("3. Bajar canal")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Salir")
            op3 = int(input("Ingrese opcion: "))
            if op3 == 1:
                control.toggle_power()
            elif op3 == 2:
                control.channel_up()
            elif op3 == 3:
                control.channel_down()
            elif op3 == 4:
                control.volumen_up()
            elif op3 == 5:
                control.volumen_down()
            elif op3 == 6:
                bandera = False
            else:
                print("Funcion incorrecta")
    elif op2 == 2:
        control: Remote = AdvancedRemote(dispositivo)
        while bandera:
            print("Funciones")
            print("1. Encender/Apagar")
            print("2. Subir canal")
            print("3. Bajar canal")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Mute")
            print("7. Salir")
            op3 = int(input("Ingrese opcion: "))
            if op3 == 1:
                control.toggle_power()
            elif op3 == 2:
                control.channel_up()
            elif op3 == 3:
                control.channel_down()
            elif op3 == 4:
                control.volumen_up()
            elif op3 == 5:
                control.volumen_down()
            elif op3 == 6:
                control.mute()
            elif op3 == 7:
                bandera = False
            else:
                print("Funcion incorrecta")
    else:
        print("Respuesta incorrecta")

elif op == 2:
    dispositivo: Device = Tv()
    print("Escoge un control")
    print("1. Control normal")
    print("2. Control avanzado")
    op2 = int(input("Ingrese opcion: "))
    if op2 == 1:
        control: Remote = Remote(dispositivo)
        while bandera:
            print("Funciones")
            print("1. Encender/Apagar")
            print("2. Subir canal")
            print("3. Bajar canal")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Salir")
            op3 = int(input("Ingrese opcion: "))
            if op3 == 1:
                control.toggle_power()
            elif op3 == 2:
                control.channel_up()
            elif op3 == 3:
                control.channel_down()
            elif op3 == 4:
                control.volumen_up()
            elif op3 == 5:
                control.volumen_down()
            elif op3 == 6:
                bandera = False
            else:
                print("Funcion incorrecta")
    elif op2 == 2:
        control: Remote = AdvancedRemote(dispositivo)
        while bandera:
            print("Funciones")
            print("1. Encender/Apagar")
            print("2. Subir canal")
            print("3. Bajar canal")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Mute")
            print("7. Salir")
            op3 = int(input("Ingrese opcion: "))
            if op3 == 1:
                control.toggle_power()
            elif op3 == 2:
                control.channel_up()
            elif op3 == 3:
                control.channel_down()
            elif op3 == 4:
                control.volumen_up()
            elif op3 == 5:
                control.volumen_down()
            elif op3 == 6:
                control.mute()
            elif op3 == 7:
                bandera = False
            else:
                print("Funcion incorrecta")
    else:
        print("Respuesta incorrecta")

elif op == 3:
    dispositivo: Device = SmartTv()
    print("Escoge un control")
    print("1. Control normal")
    print("2. Control avanzado")
    op2 = int(input("Ingrese opcion: "))
    if op2 == 1:
        control: Remote = Remote(dispositivo)
        while bandera:
            print("Funciones")
            print("1. Encender/Apagar")
            print("2. Subir canal")
            print("3. Bajar canal")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Salir")
            op3 = int(input("Ingrese opcion: "))
            if op3 == 1:
                control.toggle_power()
            elif op3 == 2:
                control.channel_up()
            elif op3 == 3:
                control.channel_down()
            elif op3 == 4:
                control.volumen_up()
            elif op3 == 5:
                control.volumen_down()
            elif op3 == 6:
                bandera = False
            else:
                print("Funcion incorrecta")
    elif op2 == 2:
        control: Remote = AdvancedRemote(dispositivo)
        while bandera:
            print("Funciones")
            print("1. Encender/Apagar")
            print("2. Subir canal")
            print("3. Bajar canal")
            print("4. Subir volumen")
            print("5. Bajar volumen")
            print("6. Mute")
            print("7. Salir")
            op3 = int(input("Ingrese opcion: "))
            if op3 == 1:
                control.toggle_power()
            elif op3 == 2:
                control.channel_up()
            elif op3 == 3:
                control.channel_down()
            elif op3 == 4:
                control.volumen_up()
            elif op3 == 5:
                control.volumen_down()
            elif op3 == 6:
                control.mute()
            elif op3 == 7:
                bandera = False
            else:
                print("Funcion incorrecta")
    else:
        print("Respuesta incorrecta")
else:
    print("Opcion incorrecta")
