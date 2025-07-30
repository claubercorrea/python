import math
try:
    R = float(input('digite o valor do raio: '))
    area = math.pi * R**2
    comprimento = 2*math.pi * R
    print(f'resultado da area {area:.2f}')
    print(f'o resultado do comprimento {comprimento:.2f}')
except:
    print('invalido')
