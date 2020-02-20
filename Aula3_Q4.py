caractere = input("Digite o caracte: ")
degraus = int(input("Digite a qtd de degraus: "))

contador = 0
escada = ""

while contador <= degraus:

    escada = caractere + escada
    print(escada)
    contador = contador + 1