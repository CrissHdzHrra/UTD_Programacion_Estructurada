peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("Oprima cualquier tecla para continuar :) ")

def agregarPeliculas():
    borrarPantalla()
    print("Agregar peliculas")
    peliculas.append(input("Ingrese la pelicula: ").upper().strip())
    print("La operaciones se realizó con exito")

def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar TODAS las peliculas")
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"{i+1}:{peliculas[i]}")
    else:
        print("No hay peliculas en este momento")

def limpiarPeliculas():
    borrarPantalla()
    print("Limpiar o borrar Todas las peliculas")
    resp=input("¿Deseas eliminar todas las peliculas del sistema? Si/No! ! !").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("¡La operacion se realizó con exito!")