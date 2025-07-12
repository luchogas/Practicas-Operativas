from manejadorColectivos import ManejadorColectivo
from manejadorTramos import manejadorTramo

def menu():
    print("\n--- MENÚ ---")
    print("a. Mostrar tramos de un chofer por DNI")
    print("b. Mostrar km y gasto estimado por colectivo")
    print("c. Listar tramos mayores a una distancia")
    print("x. Salir")

if __name__ == '__main__':
    dim = int(input("Ingrese cantidad de colectivos: "))
    mc = ManejadorColectivo(dim)
    mt = manejadorTramo()

    mc.cargar()
    mt.cargar()

    op = ''
    while op != 'x':
        menu()
        op = input("Ingrese una opción: ").lower()
        

        if op == 'a':
            dni = int(input("Ingrese DNI del chofer: "))
            mt.listado(dni, mc)
        elif op == 'b':
            mc.mostrarB(mt)
        elif op == 'c':
            tramos = float(input("Ingrese distancia: "))
            mt.tramosmayores(tramos)

        elif op == 'x':
            print("Saliendo...")
        else:
            print("Opción inválida")