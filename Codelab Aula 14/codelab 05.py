# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
#  1,68 e pese 75kg.

def imc (altura, peso):
        return peso/altura**2

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc (altura, peso)
calculoIMC = imc (altura, peso)
print(f'O Seu IMC é: {calculoIMC:.2f}')