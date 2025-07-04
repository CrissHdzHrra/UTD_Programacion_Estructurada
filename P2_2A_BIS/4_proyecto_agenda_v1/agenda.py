
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
        for nombre, datos in agenda.items():
            print(f"-"*60)
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {datos[0]}")
            print(f"Email: {datos[1]}")
        print("-"*60) 

def buscarContacto(agenda):
    borrarPantalla()
    print("\n\t:::BUSCAR CONTACTO:::")
    nombre = input("Nombre del contacto a buscar: ").upper().strip()
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"\n\tContacto encontrado:")
        print(f"-"*60)
        print(f"Nombre: {nombre}\nTeléfono: {datos[0]}\nEmail: {datos[1]}")
        print(f"-"*60)
    else:
        print("\n\tContacto no encontrado.")
        
def modificarContacto(agenda):
    borrarPantalla()
    print("\n\t:::MODIFICAR CONTACTO:::")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        nombre = input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"\n\tContacto actual: {nombre} - Teléfono: {agenda[nombre][0]}, Email: {agenda[nombre][1]}")
            nueva_tel = input("Nuevo tel.(dejar en blanco para no cambiar): ").upper().strip()
            nuevo_email = input("Nuevo email (dejar en blanco para no cambiar): ").lower().strip()
            if nueva_tel:
                agenda[nombre][0] = nueva_tel
            if nuevo_email:
                agenda[nombre][1] = nuevo_email
            print("\n\tContacto modificado con éxito.")

def eliminarContacto(agenda):
    borrarPantalla()
    print("\n\t:::ELIMINAR CONTACTO:::")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        nombre = input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(":::Valores actuales:::")
            print(f"\n\tContacto actual: {nombre}\nTeléfono: {agenda[nombre][0]}\nEmail: {agenda[nombre][1]}")
            resp=input("Desea eliminar el contacto? Si/No").lower().strip()
            if resp=="si":
                agenda.pop(nombre)
                print("Accion realizada con exito")
            else:
                print("Perfecto! gracias por su asistencia")
        else:
            print("Este contacto no existe")
    
                
