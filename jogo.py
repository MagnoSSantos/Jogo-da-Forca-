import random


def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "internet"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""

    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "

    return resultado