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

def buscarPeliculas():
    borrarPantalla()
    print("Buscar Peliculas")
    pelicula_buscar=input("Ingresa el nombre de la pelicula a buscar").upper().strip()
    if not pelicula_buscar in peliculas:
        print("Esta pelicula no existe en el sistema")
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"La pelicula {pelicula_buscar}se encontro en el casillero: {i+1}")
                encontro+=1
        print(f"Tenemos {encontro} pelicula(s) con ese titulo")
        print("La operacion se realizo con exito")

def modificarPeliculas():
        borrarPantalla()
        print("Buscar Peliculas")
        pelicula_buscar=input("Ingresa el nombre de la pelicula a buscar").upper().strip()
        if not pelicula_buscar in peliculas:
            print("Esta pelicula no existe en el sistema")
        else:
            for i in range(0,len(peliculas)):
                resp=input("¿deseas actualizar la pelicula? Si/no").lower()
                if resp=="si":
                    peliculas[i]=input("Introduce el nuevo nombre de la pelicula").upper().strip()
                    encontro+=1
                    print("La operacion se realizo con exito!")
    
        print(f"Se modifico {encontro} peliculas con este titulo")

def borrarPelicula():
    borrarPantalla()
    print("Borrar Peliculas")
    pelicula_buscar=input("Ingresa el nombre de la pelicula a buscar").upper().strip()
    if pelicula_buscar in peliculas:
        for i in range(0,len(peliculas)):
            resp=input("¿Desea quitar o borrar esta pelicula? Si/No").lower()
            if resp=="si":
                pelicula_buscar.remove[i]
                print("La operacion se realizo con exito!")
                print(f"La pelicula que se borro {pelicula_buscar} estaba en el casillero: {i+1}")
    else:
        print("Esta pelicula no existe en el sistema")
    
