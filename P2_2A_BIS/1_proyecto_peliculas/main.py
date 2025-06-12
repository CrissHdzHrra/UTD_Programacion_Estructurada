import os
os.system('cls')

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print(f"\n\t\t\t .::Gestion de peliculas::. \n\t 1-Agregar \n\t 2-Borrar"
    "\n\t 3-Modificar \n\t 4-Mostrar \n\t 5-Buscar \n\t 6-Limpiar \n\t 7-Salir")
    opcion=input("\n\t\t Eliga una opcion: ").upper

match opcion:
    case "1":
        peliculas.agregarPeliculas()
        peliculas.esperarTecla()
    case "2":
        peliculas.borrarPelicula()
        peliculas.esperarTecla()
    case "3":
        peliculas.modificarPelicula()
        peliculas.esperarTecla()
    case "4":
        peliculas.mostrarPelicula()
        peliculas.esperarTecla()
    case "5":
        peliculas.buscarPelicula()
        peliculas.esperarTecla()
    case "6":
        peliculas.limpiarPelicula()
        peliculas.esperarTecla()
    case "7":
        opcion=False
        print("Terminaste la ejecución del sistema\n .:: Gracias :")
    case _:
        print("Opción no valida, intente de nuevo")
        peliculas.esperarTecla()
        opcion=True