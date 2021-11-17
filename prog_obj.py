# class coche

class Coche:
    """Esta clase define el estado y el comportamiento de un coche"""
    ruedas = 4
    
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
    
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
    
    def pitido(self):
        print("ppiiii")
    
    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion
    
    def verVelocidad(self):
        print(self.velocidad)
    
    def __str__(self):
        return "color: " + self.color + ", aceleracion: " + str(self.velocidad) + ", ruedas: " + str(self.ruedas)
        
        
coche_rojo = Coche("rojo", 10)
coche_rojo.pitido()
coche_rojo.verVelocidad()
coche_rojo.acelera()
coche_rojo.verVelocidad()
print(str(coche_rojo))


# class animal

class Animal:
    def _init_(self, especie, edad):
        self.especie = especie
        self.edad = edad
        
    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass
    
    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass
    
    # Método genérico pero con implementación particular
    def describeme(self):
        print("Soy un animal del tipo", type(self)._name_)
        
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
        
class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")
        
class Abeja(Animal):
    def hablar(self):
        print("Bzzz")
    def moverse(self):
        print("Volando")
        
    # Nuevo método
    def picar(self):
        print("Picar!")
        
