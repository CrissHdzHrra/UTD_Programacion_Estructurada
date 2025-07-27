#asdsafjksafn

#El menu debe decir agregar, mostrar, calcular promedios y salir


import calificaciones

def main():
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        calificaciones.menuPrincipal()

        print("sistema de gestion de Calificaciones ::.. n1. -Agregar n2. -Mostrar n3. -Calcular Promedios n4. -Salir")
        opcion=input("Elige una opcion - 1/4 -")

        match opcion:
            case "1":
                calificaciones.agregarcalificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarcalificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcularpromedios(datos)
                calificaciones.esperarTecla()

            case "4":
                opcion=False

            case _:
                opcion=True
                print("opcion invalid, vuelva a intentarlo")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()