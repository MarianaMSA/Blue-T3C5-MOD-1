#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.

numero = int(input('Digite um número para a tabuada de 1x10 : '))

for i in range(1, 11) :
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')