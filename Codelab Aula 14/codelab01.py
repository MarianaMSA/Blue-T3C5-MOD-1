# Faça um programa, com uma função que necessite de três argumentos,
#  e que forneça a soma desses três argumentos.

def somar(n1, n2, n3):
    soma = n1+n2+n3
    print(f'A soma é: {soma}')

num1 = int(input('Digite o 1º nº: '))
num2 = int(input('Digite o 2º nº: '))
num3 = int(input('Digite o 3º nº: '))
somar(num1, num2, num3)