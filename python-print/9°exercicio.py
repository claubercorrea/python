import math
try:
    x1 = float(input('informe o valor de x1: '))
    x2 = float(input('informe o valor de x2: '))
    y1 = float(input('informe o valor de y1: '))
    y2 = float(input('informe o valor de y2: '))

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(f'o resultado da distancia {d:.2f}')
except:
    print('invalido')
