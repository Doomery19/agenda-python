import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
    print("# ########################################################## #")
    print("#                                                            #")
    print("#           Bienvenidos a Tus Contactos Y Eventos            #")
    print("#                                                            #")
    print("# ########################################################## #")
    print("# 1.                Gestionar Contactos                      #")
    print("# 2.                 Gestionar Eventos                       #")
    print("# 3.         Mostrar Alerta de Eventos Proximos              #")
    print("# 4.                     Salir                               #")
    print("# ########################################################## #")
    opcion = input("# Seleccione una Opcion")
    return opcion 