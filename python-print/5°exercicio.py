try:
    M = float(input('informe o seu peso: '))
    H = float(input('informe sua altura: '))
    IMC = M/H**2
    print(f'o resultado do IMC {IMC:.2f}')
except:
    print('invalido')
