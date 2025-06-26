
"""
lista= [ 
     "Ruben",10,0,10,10,0,10,0
     "Andres",8,8,9,5,6,8
]
"""

def borrarPantalla():
    import os
    os.system("clear")
def esperarTecla():
    input("Oprima una tecla para continuar")
def menuPrincipal():
    print("sistema de gestion de Calificaciones ::.. \n\1. -Agregar \n\2. -Mostrar \n\3. -Calcular Promedios \n\4. -Salir")
    opcion=input("Elige una opcion (1/4) :")
def agregarcalificaciones(lista):
    borrarPantalla()
    print("--Agregar calificaciones--")
    nombre=input("--Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range (1,4):
        continuar=True
        while continuar:
            #try:
            calificaciones.append(input(float(f"Calificaciones #1: {1}")))
            cal=input(float(f"--Calificaciones # {1}: "))
            if cal>=0 and cal<=10:
                calificaciones.append(cal)
                continuar=False
            else:
                print("--ingresar un valor comprendido entre el 0 y 10--")
            #except ValueError:
                #print ("--Ingresa un valor numerico--")
    #para concatenar se hace con ([]+variable)
    lista.append([nombre]+calificaciones)
    print("--Accion realizada con exito--")



def mostrarcalificaciones(lista):

    borrarPantalla
    print ("--Mostrar calificaciones--")
    if len(lista)>0:
        print(f{"nombre":<15} "calif. 1 calif. 2 calif. 3")
        print("-"*60)

        for fila in lista:
            print(f"{fila[0]<15}  {fila[1]<10}  {fila[2]<15}  {fila[3]<15})
        print("-"*60)
        cuantos len lista
        print son cuantos alumnos
    else:
        print("No hay registro de calificaciones en el sistema")





