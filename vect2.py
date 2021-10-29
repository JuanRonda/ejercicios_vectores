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
    

#actividad b
import random

contador = 0
lista =[]
for i in range(16):
    lista.append(random.randrange(1, 10))
for i in range(0, len(lista)):
    if(i % 3 == 0):
        contador = contador + lista[i]
        

#actividad c

    
    
