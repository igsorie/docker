from random import randrange, choice
from os import system
import time

lista_letras_elegidas = []
lista_para_mostrar = []
mylist = ["banana", "manzana", "pera", "naranja", "frutilla"]
def pedir_palabra(lista):
    return choice(lista)

def mostrar_guiones(palabra):
    for n in palabra:
        print("-", end="")
    print("\n")
def pedir_letra():
    letra = input("Ingrese la letra: ")
    return letra

def validar_letra(letra):
    if lista_letras_elegidas.count(letra) > 0:
        print("La letra ya fue elegida, eliga otra por favor")
        return False
    else:
        lista_letras_elegidas.append(letra)
        return True

def chequear_palabra(lista_letras_elegidas,lista_palabra):
    lista_para_mostrar = []
    for n in lista_palabra:
        if n in lista_letras_elegidas:
             lista_para_mostrar.append(n)
        else:
            lista_para_mostrar.append('-')
    return lista_para_mostrar

def verificar_winer(lista_palabras, lista_elegidas):
    return lista_palabras == lista_elegidas

palabra = pedir_palabra(mylist)
vidas = 6
mostrar_guiones(palabra)
print(palabra)
while(vidas > 0):
    system("cls")
    letra_elegida = pedir_letra()
    while not validar_letra(letra_elegida):
        letra_elegida = pedir_letra()
    letras = chequear_palabra(lista_letras_elegidas, list(palabra))
    print(letras)
    if verificar_winer(list(palabra), letras):
        print("Has Ganado!!!")
        break
    else:
        print("Sigue intentando")
    vidas -= 1
    print(f"Te quedan {vidas} intentos")
    time.sleep(2)
