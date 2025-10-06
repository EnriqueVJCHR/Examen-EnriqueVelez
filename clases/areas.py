
import math 

class Areas:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.radio = 0
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

    def leer_circulo(self):
        print("=== Área del Círculo ===")
        self.radio = float(input("Introduce el radio del círculo: "))
        self.area = math.pi * (self.radio ** 2)

    def mostrar_resultado(self, figura):
        print(f"\nEl área del {figura} es: {self.area:.2f}")
