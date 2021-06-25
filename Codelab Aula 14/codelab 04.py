# Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional
# de 1.5 nas horas extras trabalhadas.

def operacaoSalario (horasT, salarioT, horasE):
    if horasT > 40:
        horasE = horasT - 40
        return salarioT + (horasE * 1.5)
    else:
        return salarioT
nHorasT = float(input('Digite o nº de horas trabalhadas no mês: '))
salarioH = float(input('Digite o seu salário: '))
contaSalario = operacaoSalario(nHorasT, salarioH, 0)
print(contaSalario)
