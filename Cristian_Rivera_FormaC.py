import os

stock1 = 500
stock2 = 500
totem = [
    {
        "nombre":"Joaquin",
        "entrada": "G",
        "codigo": "Fortificado123",
    },
    {
        "nombre": "juan",
        "entrada": "PAL",
        "codigo": "ILUminador123"
    }
]



def validacion_entrada_Fortificados():
        for nombre in totem:
            if nombre ["nombre"].lower() == nombre.lower():
                print("El nombre ya existe!")
                return
        if entrada.upper() == != "G" and entrada.upper() != "V" :
            print("El tipo de entrada debe ser : [G] O [V]")
        if len(codigo) != 6:
            print("El codigo de verificacion debe contener almenos 6 caracteres.")
        print("Entrada registrada!")
        validacion_entrada_Fortificados
        print(" *** COMPRA DE ENTRADA PARA LOS FORTIFICADOS *** ")
def comprar_entradas_ILUMINADOS():

    print(" *** COMPRA DE ENTRADAS PARA LOS ILUMINADOS *** ")
    nombre = input(" Ingrese nombre del comprador: ")
    entrada = input(" Ingrese tipo de entrada (CV/PAL): ")
    codigo = input(" Ingrese codigo de confirmacion: ")


def validacion_entrada_ILUMINADOS():
    if entrada() == "CV" and "G":
        print(" El tipo de entrada debe ser : [CV] O [PAL]")
    if codigo(len) != 6:
        print("El codigo de verificacion debe contener almenos 6 caracteres.")
    for nombre in totem:
        if nombre["nombre"].lower() == nombre.lower():
            print("El nombre ya existe")
        return
    print("Entrada registrada!")


    


while True:
    print("[1] Comprar entrada a “los Fortificados” ")
    print("[2] Comprar entrada a “los Iluminados”. ")
    print("[3] Stock de entradas para ambos conciertos ")
    print("[4] Salir")
    try:
        opcion = input ("[1-4] Ingresa una opcion: ")
    except ValueError:
        print("Debes ingresar un valor valido")
    


    if opcion == "1":
        nombre = input("Nombre: ")
        entrada = input("Ingresa tu tipo de entrada [G/V]")
        codigo = input("Ingrese codigo de confirmacion: ")
    elif opcion == "2":
        nombre = input("Nombre: ")
        entrada = input("Ingresa tu tipo de entrada [CV/PAL]")
        codigo = input("Ingrese codigo de confirmacion: ")

    elif opcion == "3":
        print("El stock de ambos conciertos es")
        print(f"El stock es {stock1}")
        print(f"El stock es {stock2}")

    elif opcion == "4":

        print("Programa terminado!")
        break
    else:
        print("Seleccion no valida!")




