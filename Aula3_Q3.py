import random

lista = []
qtd = int(input("informa a qtd de digitos: "))
contador = 0

if qtd <= 0:
    print("Qtd inválida")
else:
    while contador <= qtd:

        numero = random.randrange(1,100)
        lista.append(numero)
        contador = contador + 1

    print("Essa é a lista: ", lista)
    print("Esse é o valor máximo: ", max(lista))
    print("Esse é o valor minimo: ", min(lista))