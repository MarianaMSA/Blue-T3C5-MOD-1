# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:
def area(num1, num2):
        terreno = num1*num2
        print(f'A area do terreno é /; {terreno} m²')

largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o  comprimento: '))
area(largura, comprimento)


