try:
    L = float(input('informe o lado do cubico em metros: '))
    H = float(input('informe a altura do preenchida do combustivel em metros: '))
    volume = L**2 * H
    volumeLitro = volume * 1000
    autonomia = volumeLitro*10
    print(f'volume do combustivel {volumeLitro:.2f} litros')
    print(f'distancia maxima de autonomia: {autonomia:.2f}')
except:
    print('invalido')
