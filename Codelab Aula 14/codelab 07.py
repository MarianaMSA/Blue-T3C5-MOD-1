# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.

def comparacao (n1, n2):
    if n1 < n2:
        return n1
    elif n2 < n1:
        return n2
    else: 
        return 'Os números são iguais'

num1 = float(input('Digite o 1º nº: '))
num2 = float(input('Digite o 2º nº: '))
comparacao(num1, num2)
comparando = comparacao(num1, num2)
print(comparando)