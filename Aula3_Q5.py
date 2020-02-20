import statistics
pi = statistics.math.pi

raio = input("Informe o raio: ")

if not raio.isdigit():
    print("Inserir um valor numérico!")
else:
    area = pi*int(raio)**2
    comprimento = 2*(pi*int(raio))

print("Área: ", area)
print("Comprimento: ", comprimento)