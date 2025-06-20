#Dict u objeto que permita almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero, idioma)

#pelicula = {
#    "nombre": "",
#    "categoria": "",
#    "clasificacion": "",
#    "genero": "",
#    "idioma": ""
#    "........."
pelicula={}

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t Presiona una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t Agregar Peliculas")
    pelicula.update({"nombre": input("\n\t Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("\n\t Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion": input("\n\t Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero": input("\n\t Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma": input("\n\t Ingresa el idioma: ").upper().strip()})
    print("\n\t LA OPERACION SE REALIZO CON EXITO")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t Mostrar Peliculas")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\n\t {i}: {pelicula[i]}")
    else:
        print("\n\t No hay peliculas registradas")

def borrarPelicula():
    borrarPantalla()
    print("\n\t\t\t\t Borrar o Quitar la Pelicula")
    if len(pelicula) > 0:
        resp= input("\n\t Deseas borrar la pelicula? (Si/Nn): ").upper().strip()
        if resp == "Si":
            pelicula.clear()
            print("\n\t La pelicula se ha borrado con exito")
    else:
        print("\n\t No hay peliculas registradas")

            
def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t Agregar Caracteristica a la Pelicula")
    if len(pelicula) > 0:
        atributo = input("\n\t Introduzca el nombre de la caracteristica quedeseas agregar: ").lower().strip()
        valor_atributo = input(f"\n\t Introduzca el valor para {atributo}: ").upper().strip()
        pelicula[atributo] = valor_atributo
        print("\n\t¡¡¡La caracteristica se ha agregado con exito!!!")

"""
#Parte del examen -Simulacro-
def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t Modificar Caracteristica de la Pelicula")
    if len(pelicula) > 0:
        respuesta="si"
        while respuesta=="si":
            for i in pelicula:
                print(f"\n\t {i}: {pelicula[i]}")
                respuesta= input(f"\n\t Deseas modificar la caracteristica de {i}? (Si/No): ").upper().strip()
                if respuesta == "si":
                    n_valor = input(f"\n\t Introduzca el nuevo valor para {i}: ").upper().strip()
                    pelicula[i] = n_valor
                    print("\n\t¡¡¡Haz modificado la caracteristica con exito!!!")
    else:
        print("\n\t No hay peliculas registradas")
"""

"""
#borrar caracteristica
def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t Borrar Caracteristica de la Pelicula")
    if len(pelicula) > 0:
        respuesta="si"
        while respuesta=="si":
            for i in pelicula:
                respuesta=input(f"\n\t Deseas borrar el valor de {i}? (Si/No): ").upper().strip()
                if respuesta == "si":
                    pelicula[i].clear()
"""