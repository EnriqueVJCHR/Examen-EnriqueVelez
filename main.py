

from clases.areas import Areas 

def main():
    obj = Areas()

    print("=== CÁLCULO DE ÁREAS ===")
    print("1. Triángulo")
    print("2. Rectángulo")

    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        obj.leer_triangulo()
        obj.mostrar_resultado("triángulo")
    elif opcion == "2":
        obj.leer_rectangulo()
        obj.mostrar_resultado("rectángulo")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
