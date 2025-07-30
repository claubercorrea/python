import math
try:
    R = float(input('digite o valor do raio: '))
    volumeEsfera = (4/3) * math.pi*R**3
    print(f' o resultado do volumeEsfera {volumeEsfera:.2f}')
except:
    print('invalido')