
def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("\n\t\t::::Oprima cualquier tecla para continuar....::::")

def menuPrincipal():
    print(":::☻SISTEMA DE GESTION DE AGENDA DE CONTACTOS☻:::")
    print("\n\t1. Agregar contacto")
    print("\t2. Mostrar todos los contactos")
    print("\t3. Buscar contacto por nombre")
    print("\t4. Salir")
    opcion = input("\n👉 Selecciona una opción de 1-4: ").upper()
    return opcion

def agregarContacto(agenda):
    borrarPantalla()
    print("\n\t:::AGREGAR CONTACTOS:::")
    nombre=input("Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\tEste contacto ya existe")
    else:
        tel=input("Telefono: ").upper().strip()
        email=input("Email: ").lower().strip()
        agenda[nombre]=[tel,email]
        print("\n\tAccion Realizada con exito")

def mostrarContactos(agenda):
    borrarPantalla()
    print("\n\t:::MOSTRAR CONTACTOS:::")
    if not agenda:
        print("No hay contactos registrados::...")
    else:
        for i in agenda:
            print(f"{i} {agenda[i]}")
