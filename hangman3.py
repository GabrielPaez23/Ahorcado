import random
import os

ahorcado = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

with open("./archivos/data.txt", "r", encoding="utf-8" ) as f:
    diccionario = [i.upper().rstrip("\n") for i in f]
    #Creacion de nueva lista con las palabras del archivo data
"""""palabra, tablero, intentos = iniciar_juego(dicionario)
variables a utilizar(posible cambio)
"""""

def iniciar_juego(diccionario):
    palabra = random.choice(diccionario)
    tablero = ["_"] * len(palabra)
    intentos = 5
    return palabra, tablero, intentos
#eleccion aleatoria de la palabra, creacion del tablero asignacion de los intentos


def arreglo(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
#quitar los acentos

def pedir_letra():
#posible agregar letra repetida y solucion de error
    valido = False
    while not valido:
        letra = input("Porfavor ingrese una letra: ").upper()
        valido = "A" <= letra <= "Z" and len(letra) == 1
        if not valido:
            print("Solo puedes un caracter y que sea una letra")
    return letra
    

def imprimir_tablero(tablero, intentos):
    for caracter in tablero:
        print(caracter, end=" ")
    print(ahorcado[intentos])
    print() 
    print()
#Se imprime el tablero
    

def procesar_letra(palabra, tablero, intentos):
#Se hace todo el proceso de si la letra es correcta y la repeticion con un bucle
    while tablero != palabra and intentos != 0:
        imprimir_tablero(tablero,intentos)
        letras_encontradas = False
        letra = pedir_letra()
        os.system("cls")
        for indice, caracter in enumerate(palabra):
            if caracter == letra:
                tablero[indice] = letra
                letras_encontradas = True

        if not letras_encontradas:
            intentos -= 1
            

        if not "_" in tablero:
            print("Ganaste la letra era " + palabra)
            break
    
        elif intentos == 0:
            print("Perdiste la letra era " + palabra)
            break


def run():
    palabra, tablero, intentos = iniciar_juego(diccionario)
    procesar_letra(palabra,tablero,intentos)
    
        


if __name__ == "__main__":
    run()