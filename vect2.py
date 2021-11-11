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


#otra forma
#valores de la serie fibonacci
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

def fibonacci(n):
    if(n == 1):
        return 1
    if(n == 0):
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
#apartado d,e,f

'''Con valores introducidos por el usuario, y acontinuacion
que los imprima al reves'''
#hacer la funcion
def apartado_d():
    #inicializar una lista vacia
    x = 0
    lista = []
    lista_aux = []
    for i in range(0,15):
        valor = int(input("Dime un valor: "))
        lista.append(valor)
  
    
    for i in range(14, 0, -1):
        lista_aux.append(lista[i])
        
    
    print(lista_aux)
        

def test():
    for i in range(14, -1, -1):
        print(i)
        
        

def apartado_d_b():
    vector = []
    i = 0
    while(i < 15):
        x = int(input("Escribe un número: "))
        vector.append(x)
        i += 1
    vector.reverse()
    print(vector)
    
    
    
    
def apartado_d_c():
    lista1 = []
    lista2 = []
    n = 14
    while(len(lista1) < 15):
        print("Introduce los valores: ")
        x = int(input())
        lista1.append(x)
    print(lista1)
    while(n >= 0):
        o = lista1[n]
        lista2.append(o)
        n = n- 1
    print(lista2)
        
    
    
'''e) Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta
que esté entre 1 o 10. (Nota: Lista de 15 elementos)
'''
def apartado_e():
    print("Apartado e")
    x = 0
    list = []
    for e in range(0,15):
        print("Escribe un número entre 1 y 10")
        x = int(input())
        while((x < 11) and (x > 0)):ç
        if((x < 11) or (x > 0)):
            list.append(x)
        else:
            print("Dime otro número:")
    
    print(list)
    
    
    
    
    
def apartado_eb():
    numeros = []
    x = 0
    print("Dime 15 números entre 1 y 10")
    while(x < 15):
        a = int(input("Dime un número:"))
        if((a <= 10) or (a >= 0)):
            numeros.append(a)
            x = x + 1
        else:
            print("Dime otro número:")
    return numeros
    
    
    
 
    
'''f) Con valores introducidos por el usuario, que deben formar una secuencia creciente.'''


def apartado_f():
    num = 0
    aux = 0
    contador = 0
    list = []
    
    

    
#genera_matriz

def generaMatriz(num_f, num_c, valor):
    return [[valor for c in range(0, num_c)] for f in range(0, num_f)]


#matriz

matriz = [[1,0,0],[0,-5,0],[0,0,2]]
vector = [1,0,2]

#sin indices
'''
for fila in matriz:
    for elemento in fila:
        print(elemento)
'''

#con indices
'''
for indice1 in range(0, len(matriz)):
    for indice2 in range(0, len(matriz[indice1])):
        print(matriz[indice1][indice2])
'''
        
    
    
#tres en raya

a = [['-','O','-'], ['-','-','O'], ['X','X','-']]

#hacemos que nos lo imprima paso a paso, cada fila y columna usando las matrices
def imprime(matriz):
    print("-------------")
    print("| ", matriz[0][0], "|", matriz[0][1], "|" , matriz[0][0])
    print("-------------")
    print("| ", matriz[1][0], "|", matriz[1][1], "|" , matriz[1][2])
    print("-------------")
    print("| ", matriz[2][0], "|" , matriz[2][1], "|", matriz[2][2])
    print("-------------")
    
    





    
    
