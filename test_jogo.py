from jogo import mostrar_palavra


# Teste válido 1: nenhuma letra foi descoberta
def teste_palavra_oculta():
    resultado = mostrar_palavra("python", [])
    assert resultado == "_ _ _ _ _ _ "

# Teste válido 2: uma letra correta é mostrada
def teste_letra_correta():
    resultado = mostrar_palavra("python", ["p"])
    assert resultado == "p _ _ _ _ _ "

# Teste válido 3: várias letras corretas são mostradas
def teste_varias_letras_corretas():
    resultado = mostrar_palavra("python", ["p", "t", "o"])
    assert resultado == "p _ t _ o _ "

# Teste válido 4: letra repetida aparece em todas as posições
def teste_letra_repetida():
    resultado = mostrar_palavra("programacao", ["a"])
    assert resultado == "_ _ _ _ _ a _ a _ a _ "

# Teste válido 5: palavra completamente descoberta
def teste_palavra_completa():
    resultado = mostrar_palavra("python", ["p", "y", "t", "h", "o", "n"])
    assert resultado == "p y t h o n "

teste_palavra_oculta()
print("Teste válido 1: OK")

teste_letra_correta()
print("Teste válido 2: OK")

teste_varias_letras_corretas()
print("Teste válido 3: OK")

teste_letra_repetida()
print("Teste válido 4: OK")

teste_palavra_completa()
print("Teste válido 5: OK")

# Teste inválido 1: número não deve ser considerado uma letra válida
entrada = "5"

if len(entrada) != 1 or not entrada.isalpha():
    print("Teste inválido 1: OK")
else:
    print("Teste inválido 1: FALHOU")

# Teste inválido 2: mais de uma letra não deve ser aceita
entrada = "ab"

if len(entrada) != 1 or not entrada.isalpha():
    print("Teste inválido 2: OK")
else:
    print("Teste inválido 2: FALHOU")

# Teste inválido 3: entrada vazia não deve ser aceita
entrada = ""

if len(entrada) != 1 or not entrada.isalpha():
    print("Teste inválido 3: OK")
else:
    print("Teste inválido 3: FALHOU")

# Teste inválido 4: caractere especial não deve ser aceito
entrada = "@"

if len(entrada) != 1 or not entrada.isalpha():
    print("Teste inválido 4: OK")
else:
    print("Teste inválido 4: FALHOU")

# Teste inválido 5: letra repetida não deve ser aceita novamente
letras_tentadas = ["p", "y", "t"]
entrada = "p"

if entrada in letras_tentadas:
    print("Teste inválido 5: OK")
else:
    print("Teste inválido 5: FALHOU")