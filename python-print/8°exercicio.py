import math
try:
    R = float(input('digite o raio do tanque(em metros): '))
    H = float(input('digite a altura do tanque (em metros): '))
    area = 2*math.pi * R * (H*R)
    litroNecessario = area / 3
    lata = math.ceil(litroNecessario / 5)
    custoTotal = lata * 50
    print(f'total a ser pintado {area:.2f}')
    print(f'litro de tinta necessario {litroNecessario:.2f}')
    print(f'lata de tinta necessaria {lata:.2f}')
    print(f'custo total {custoTotal:.2f}')
except:
    print('invalido')
