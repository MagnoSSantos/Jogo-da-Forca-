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

def jogar():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_tentadas = []
    tentativas = 6

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas))
        print("Tentativas restantes:", tentativas)

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra.")
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            letras_corretas.append(letra)
            print("Você acertou!")
        else:
            tentativas -= 1
            print("Você errou!")

        if all(letra in letras_corretas for letra in palavra):
                print("\nParabéns! Você venceu!")
                print("A palavra era:", palavra)
                return
    print("\nVocê perdeu!")
    print("A palavra era:", palavra)

jogar()          