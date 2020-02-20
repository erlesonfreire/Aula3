import statistics

pi = statistics.math.pi

def area_circulo(raio):
    area = pi*(int(raio)**2)
    return area

def comprimento_circulo(raio):
    comprimento = 2*pi*int(raio)
    return comprimento

r = input('Informe o raio: ')

if not r.isdigit():
    print('Insira um valor numérico!')
else:    
    resultado_area = round(area_circulo(r),2)
    resultado_comprimento = round(comprimento_circulo(r),2)
    print('Uma circulo de raio', r, 'tem área de', resultado_area, 'e um comprimento de', resultado_comprimento)
