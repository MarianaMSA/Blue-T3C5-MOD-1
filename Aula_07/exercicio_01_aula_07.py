# #01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

menor = 0
maior = 0


for p in range(1, 6) :
        peso = int(input('Peso da {} pessoa:'.format(p)))
        if p == 1 :
                maior = peso
                menor = peso
        else:
                if peso > maior :
                        maior = peso
                elif peso < menor :
                        menor = peso

print(f'{maior} é o maior peso')

print(f'{menor} é o menor peso')

