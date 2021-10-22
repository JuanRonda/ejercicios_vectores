# a va a imprimir  2, 4, 6
'''
Se pide que a se repita 2 veces.
Se guarda el valor en la a (lista), a continuación se le da el valor de 2 a a[0], luego se hace otro
apartado de a[1] y se le dará el valor de 2x2 = 4, y al final de la lista se añade otro elemento que será la suma de a[0] y a[1]
'''

a =  [0] * 2
b = [0, 0, 0]
a[0] = 2
a[1] = a[0] ** a[0]
a.append( a[0] + a[1] )

print(a)
