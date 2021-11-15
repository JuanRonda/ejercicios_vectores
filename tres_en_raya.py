estado_inicial = [[0,0,0],[0,0,0],[0,0,0]]
estado_actual = [[0,'X',0],[0,0,'X'],['O','O',0]]

#hacemos que nos lo imprima paso a paso, cada fila y columna usando las matrices
def imprime(matriz):
    print("-------------")
    print("| ", matriz[0][0], "|", matriz[0][1], "|" , matriz[0][0])
    print("-------------")
    print("| ", matriz[1][0], "|", matriz[1][1], "|" , matriz[1][2])
    print("-------------")
    print("| ", matriz[2][0], "|" , matriz[2][1], "|", matriz[2][2])
    print("-------------")
    
imprime(estado_actual)

def hayFicha(estado_actual, pos_fila, pos_columna):
    return estado_actual[pos_fila][pos_columna] == 1 or estado_actual

print(hayFicha(estado_actual, 0,1)) #1 --> True
print(hayFicha(estado_actual, 2,1)) #2 --> True
print(hayFicha(estado_actual, 2,2)) #3 --> False

def ponerFicha(estado_actual, pos_fila, pos_columna, ficha):
    return estado_actual[pos_fila][pos_columna] == ficha

def introducirFicha(estado_actual, pos_fila, pos_columna, ficha):
    if(not hayFicha(estado_actual, pos_fila, pos_columna)):
        ponerFicha(estado_actual,  pos_fila, pos_columna, ficha)
        print("OK")
    else:
        print("Lo sentimos, hay una ficha prueba con otra posición")

'''
fin = False
turno = 1 #1 -> Jugador A .  2 -> Jugador B
while(not fin):
    print("Le toca al Jugador ", turno)
'''
    
#La funcion ganador devuelve:
#   1 - si el jugador que ha ganado es A
#   2 - si el jugador que ha ganado es B
#   3 - Hay tablas
#   4 - Se esta jugando
def ganador(matriz):
    # X
    if((matriz[0][0] == 'X') and (matriz[0][1] == 'X') and (matriz[0][2] == 'X') 
       or (matriz[1][0] == 'X') and (matriz[1][1] == 'X') and (matriz[1][2] == 'X')
       or (matriz[2][0] == 'X') and (matriz[2][1] == 'X') and (matriz[2][2] == 'X')
       or (matriz[0][0] == 'X') and (matriz[1][0] == 'X') and (matriz[2][0] == 'X')
       or (matriz[0][1] == 'X') and (matriz[1][1] == 'X') and (matriz[2][1] == 'X')
       or (matriz[0][2] == 'X') and (matriz[1][2] == 'X') and (matriz[2][2] == 'X')):
        pass
