
class Areas:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.area = 0

    def leer_triangulo(self):
        print("=== Área del Triángulo ===")
        self.base = float(input("Introduce la base del triángulo: "))
        self.altura = float(input("Introduce la altura del triángulo: "))
        self.area = (self.base * self.altura) / 2

    def leer_rectangulo(self):
        print("=== Área del Rectángulo ===")
        self.base = float(input("Introduce la base del rectángulo: "))
        self.altura = float(input("Introduce la altura del rectángulo: "))
        self.area = self.base * self.altura

    def mostrar_resultado(self, figura):
        print(f"\nEl área del {figura} es: {self.area}")
