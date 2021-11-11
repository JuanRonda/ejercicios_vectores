'''
4.- Crea un programa llamado vect4.py, en el que el usuario introduzca un número entero y el
programa genere una frase con las palabras correspondientes a cada cifra. 

Por ejemplo, 547 devolvería “cinco cuatro siete”.
'''

def frase(numero):
    res = ""
    #print(type(numero))
    str_numero = str(numero)
    #print(type(str_numero))
    #print(str_numero[0])
    #print(len(str_numero))
    index = 0
    while(index < len(str_numero)):
        #print(index)
        if(str_numero[index] == '0' ):
            res = res + "cero "
        elif(str_numero[index] == '1' ):
            res = res + "uno "
        elif(str_numero[index] == '2' ):
            res = res + "dos "
        elif(str_numero[index] == '3' ):
            res = res + "tres "
        elif(str_numero[index] == '4' ):
            res = res + "cuatro "
        elif(str_numero[index] == '5' ):
            res = res + "cinco "
        elif(str_numero[index] == '6' ):
            res = res + "seis "
        elif(str_numero[index] == '7' ):
            res = res + "siete"
        elif(str_numero[index] == '8' ):
            res = res + "ocho "
        else:
            res = res + "nueve "
        index = index + 1
    return res
  
  
  
#otra forma

def frase2(numero):
    res = ""
    #print(type(numero))
    str_numero = str(numero)
    #print(type(str_numero))
    #print(str_numero[0])
    #print(len(str_numero))
    index = 0
    for i in str_numero:
        #print(index)
        if(i == '0' ):
            res = res + "cero "
        elif(i == '1' ):
            res = res + "uno "
        elif(i == '2' ):
            res = res + "dos "
        elif(i == '3' ):
            res = res + "tres "
        elif(i == '4' ):
            res = res + "cuatro "
        elif(i == '5' ):
            res = res + "cinco "
        elif(i == '6' ):
            res = res + "seis "
        elif(i == '7' ):
            res = res + "siete"
        elif(i == '8' ):
            res = res + "ocho "
        else:
            res = res + "nueve "
    return res
  
  
  
