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
        

        
        
#guerrrero

import random
class guerrero:
    def __init__(self, nombre, vida, fuerza, precisión, velocidad, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.precisión = precisión
        self.velocidad = velocidad
        self.defensa = defensa
        
    def golpear(self,g):
        # veo si acierto el golpe
        if(random.random() <= (self.precisión - g.velocidad) / 100):
            #en caso de acertar, agrego dañoa al oponente
            g.vida -= max([(self.fuerza - g.defensa) + random.randrange(-10,11),1])
            print("Golpe certero de", self.nombre)
        else:
            print(g.nombre, "esquiva el golpe!")
            
def simular_batalla(j1,j2):
    #comienza jugador más veloz
    golpeador,receptor = j1, j2
    if(j1.velocidad < j2.velocidad):
        golpeador,receptor = j2, j1
    #se golpean hasta que alguno tenga vida cero
    while(j1.vida > 0 and j2.vida > 0):
        print("\n" + j1.nombre,j1.vida, "vs", j2.vida,j2.nombre)
        golpeador.golpear(receptor)
        #cambio de turnos
        golpeador,receptor = receptor,golpeador
    #fin
        print("\n" + j1.nombre,j1.vida, "vs", j2.vida,j2.nombre)
        print("Ganador", receptor.nombre)
              
#batalla de ejemplo
superman = guerrero("Superman",100,50,80,30,20)
goku = guerrero("Gokú",100,60,80,40,20)
chuck = guerrero("Chuck Norris",200,99,99,99,99)

#simula batalla
simular_batalla(goku,chuck)
