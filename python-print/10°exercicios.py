import math
try:
    r = float(input('informe o valor do raio: '))
    h = float(input('informe a altura :'))
    consumoHora = 1350

    volume = math.pi * r**2*h
    volumelitro = volume * 1000

    autonomia = volumelitro / consumoHora
    print(f'volume em litro da caixa de agua {volumelitro:.2f}')
    print(f'autonomia {autonomia:.2f}')
except:
    print('invalido')
