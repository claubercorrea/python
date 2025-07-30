
try:
    desconto = 0.11
    impostoRenda = 0.08
    inss = 0.05
    ganhaHora = float(input('informe quanto ganha a hora:  '))
    horasTrabalhadas = float(input('informe quantas horas trabalhada'))
    salarioBruto = ganhaHora * horasTrabalhadas
    salarioLiquido = salarioBruto - desconto - impostoRenda - inss
    print(f' salario bruto {salarioBruto:.2f}')
    print(f'salario liquido {salarioLiquido:.2f}')
except:
    print('invalido')
