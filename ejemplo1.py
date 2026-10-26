#Ejercicio 

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonidos(self):
        pass

class Conejo(Animal):
    def hacer_sonidos(self):
        return "Hola soy un conejo"
    
mi_conejo = Conejo("Rabbit")
#print(mi_conejo.nombre)
#print(mi_conejo.hacer_sonidos())

#Ejemplo 2 - herencia multiple
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return "Bruuuummmm"
    
# class Persona(Vehiculo, Animal):
#     def __init__(self, nombre, marca, modelo):
#         Vehiculo.__init__(self, marca, modelo)
#         Animal.__init__(self, nombre)

#     def presentarse(self):
#         return(f"Hola, soy {self.nombre} y conduzco un {self.marca} {self.modelo}")
    
# persona1 = Persona("David", "Hyundai", "i30")
# print(persona1.presentarse())
# print(persona1.conducir())

#Clases compuestas
class Persona:
    def __init__(self, nombre, vehiculo, animal):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.animal = animal 
        
    def presentarse(self):
        return f"Soy {self.nombre} de la marca {self.vehiculo.marca} {self.vehiculo.modelo} y mi mascota se llama {self.animal.nombre}"
    
vehiculo1 = Vehiculo("Hyundai", "i30")
animal1 = Animal("Rabbit")
persona2 = Persona("David", vehiculo1, animal1)
print(persona2.presentarse())
print(persona2.vehiculo.conducir())
