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

lista =[]
for i in range(16):
    lista.append(random.randrange(1, 10))
acumulador = 0
for i in range(0,15):
    if(i % 3 == 0):
        acumulador = acumulador + lista[i]
    print(lista)
    print("acumulador: ", acumulador)
        

#actividad c

import random

lista =[]
for i in range(16):
    lista.append(random.randrange(1, 10))
    
#inicializar las variables

def apartado_c(lista):
    n = len(lista)
    f = [0,1]
    x = 0
    res = 0
    
    for i in f:
        res = res + i
        f.append(res)
        x += 1
        if(x == n):
            break
    f.pop(0)
    f.pop(0)
    return f

    
    
