
def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("\n\t\t::::Oprima cualquier tecla para continuar....::::")

def menuPrincipal():
    print(":::SISTEMA DE GESTION DE AGENDA DE CONTACTOS 📞:::")
    print("\n\t1. ➕ Agregar contacto")
    print("\t2. 🗒️ Mostrar todos los contactos")
    print("\t3. 🔍 Buscar contacto por nombre")
    print("\t4. ✍️ Modificar contacto")
    print("\t5. 🗑️ Eliminar contacto")
    print("\t6. 🚪 Salir")
    opcion = input("\n:::👉 Selecciona una opción::: ").strip()
    return opcion

def agregarContacto(agenda):
    borrarPantalla()
    print("\n\t:::➕ AGREGAR CONTACTOS :::")
    nombre = input("Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t:::⚠️ Este contacto ya existe.:::")
    else:
        tel = input("Teléfono: ").strip()
        email = input("Email: ").lower().strip()
        agenda[nombre] = [tel, email]
        print("\n\t✅ ¡Acción Realizada con éxito!")

def mostrarContactos(agenda):
    borrarPantalla()
    print("\n\t:::🗒️ MOSTRAR CONTACTOS :::")
    if not agenda:
        print("¡No hay contactos registrados aún! 😔")
    else:
        for nombre, datos in agenda.items():
            print(f"-"*60)
            print(f"👤 Nombre: {nombre}")
            print(f"📞 Teléfono: {datos[0]}")
            print(f"📧 Email: {datos[1]}")
        print("-"*60) 

def buscarContacto(agenda):
    borrarPantalla()
    print("\n\t:::🔍 BUSCAR CONTACTO :::")
    nombre = input("Nombre del contacto a buscar: ").upper().strip()
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"\n\tContacto encontrado: ✨")
        print(f"-"*60)
        print(f"👤 Nombre: {nombre}\n📞 Teléfono: {datos[0]}\n📧 Email: {datos[1]}")
        print(f"-"*60)
    else:
        print("\n\tContacto no encontrado. 😔")

def modificarContacto(agenda):
    borrarPantalla()
    print("\n\t:::✍️ MODIFICAR CONTACTO :::")
    if not agenda:
        print("¡No hay contactos en la agenda para modificar! 😔")
    else:
        nombre = input("Nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print(f"\n\tContacto actual: 👤 {nombre} - 📞 {agenda[nombre][0]}, 📧 {agenda[nombre][1]}")
            nueva_tel = input("Nuevo teléfono (dejar en blanco para no cambiar): ").strip()
            nuevo_email = input("Nuevo email (dejar en blanco para no cambiar): ").lower().strip()
            
            if nueva_tel:
                agenda[nombre][0] = nueva_tel
            if nuevo_email:
                agenda[nombre][1] = nuevo_email
            
            print("\n\t✅ ¡Contacto modificado con éxito!")
        else:
            print("\n\tContacto no encontrado. 😔")

def eliminarContacto(agenda):
    borrarPantalla()
    print("\n\t:::🗑️ ELIMINAR CONTACTO :::")
    if not agenda:
        print("¡No hay contactos en la agenda para eliminar! 😔")
    else:
        nombre = input("Nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            print("\n\t:::Valores actuales:::")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 Email: {agenda[nombre][1]}")
            resp = input("¿Desea eliminar este contacto? (Si/No): ").lower().strip()
            if resp == "si":
                del agenda[nombre]
                print("\n\t:::🗑️ ¡Contacto eliminado con éxito!:::")
            else:
                print("\n\t:::❌ Operación cancelada. El contacto no fue eliminado:::...")
        else:
            print("\n\t:::Contacto no encontrado::...")
