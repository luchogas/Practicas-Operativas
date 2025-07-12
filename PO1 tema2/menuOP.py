from gestorGastos import GestorGastos
from gestorMovilidad import GestorMovilidad

def menu():
    print("\n--- MENÚ ---")
    print("a. Listar gastos por patente")
    print("b. Gastos en una fecha específica")
    print("c. Resumen por movilidad en una fecha")
    print("x. Salir")

if __name__ == '__main__':
    gg = GestorGastos()
    gm = GestorMovilidad()

    gg.cargar()
    gm.cargar()
    
    op = ''
    while op != 'x':
        menu()
        op = input("Ingrese opción: ").lower()

        if op == 'a':
            patente = input("Ingrese patente: ").upper()
            gm.listarPatente(patente, gg)
        elif op == 'b':
            fecha = input("Ingrese fecha (dd/mm/aaaa): ")
            gg.mostrar_por_fecha(fecha)
        elif op == 'c':
            fecha = input("Ingrese fecha (dd/mm/aaaa): ")
            gg.resumen_por_fecha(fecha, gm)
        elif op == 'x':
            print("Saliendo...")
        else:
            print("Opción inválida")
