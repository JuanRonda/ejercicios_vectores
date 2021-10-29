#actividad a
import random

n_impares = 0
n_pares = 0
lista = []
for i in range(15):
    lista.append(random.randrange(1,10))
for i in lista:
    if(i % 2 == 0):
        n_pares += 1
    else:
        n_impares += 1
    

    
    
