try:
    tamanhoArquivo = float(input('informe o tamanho do arquivo: '))
    velocidadeArquivo = float(input('informe a velocidade do arquivo: '))
    tempototalSegundos = tamanhoArquivo / velocidadeArquivo
    minutos = round(tempototalSegundos//3600)
    segundos = round(tempototalSegundos % 60)

    print(f'tempo de dowloand  minutos 10{minutos} : {segundos}')
except:
    print('invalido')
