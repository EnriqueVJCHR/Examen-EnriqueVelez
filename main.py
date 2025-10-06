
from clases.areas import Areas

def main():
    obj = Areas()

    print("=== CÁLCULO DE ÁREAS ===")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Círculo")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        obj.leer_triangulo()
        obj.mostrar_resultado("triángulo")
    elif opcion == "2":
        obj.leer_rectangulo()
        obj.mostrar_resultado("rectángulo")
    elif opcion == "3":
        obj.leer_circulo()
        obj.mostrar_resultado("círculo")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
