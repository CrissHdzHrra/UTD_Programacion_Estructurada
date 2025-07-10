import agenda


def main():
    agenda_contactos = {}
    opcion = True
    while opcion:
        agenda.borrarPantalla()
        agenda.menuPrincipal()
        opcion = input("\t\tElige una opcion: ").strip() # Added input to capture user choice

        if opcion == "1":
            agenda.agregarContacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "2":
            agenda.mostrarContactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "3":
            agenda.buscarContacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "4":
            agenda.modificarContacto(agenda_contactos) # New: Modificar contacto
            agenda.esperarTecla()
        elif opcion == "5":
            agenda.borrarContacto(agenda_contactos) # New: Borrar contacto
            agenda.esperarTecla()
        elif opcion == "6":
            agenda.borrarPantalla()
            print("Programa Finalizado")
            opcion = False
        else:
            print("\t\t:::Opcion no valida, vuelva a intentarlo 🚫⚠️:::")
            agenda.esperarTecla()

if __name__ == "__main__":
    main()

