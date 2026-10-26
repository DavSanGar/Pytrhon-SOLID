class Figura():
    def obtener_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def obtener_area(self):
        return self.ancho * self.alto
    
    def set_ancho(self, ancho):
        self.ancho = ancho
    def set_alto(self, alto):
        self.alto = alto

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def set_lado(self, lado):
        self.lado = lado

    def obtener_area(self):
        return self.lado * self.lado

def imprimir_area(figura:Figura):
    print(f"Area:{figura.obtener_area()}")

rectangulo = Rectangulo(4,5)
cuadrado = Cuadrado (4)

imprimir_area(rectangulo)
imprimir_area(cuadrado)

#print(f"El area del rectangulo es: {area_rectangulo}")
#print(f"El area del cuadrado es: {area_cuadrado}")