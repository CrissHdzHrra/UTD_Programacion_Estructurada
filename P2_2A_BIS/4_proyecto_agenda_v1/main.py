import agenda



def main():
    agenda_contactos={}
    opcion=True
    while opcion:
        agenda.borrarPantalla()
        agenda.menuPrincipal()

        if opcion=="1":
            agenda.agregarContacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="2":
            agenda.mostrarContactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="4":
            agenda.borrarPantalla()
            print("Programa Finalizado")
            opcion=False
        else:
            opcion=True
            print("\t\t:::Opcion no valida, vuelva a intentarlo:::")


if __name__=="__main__":
    main()