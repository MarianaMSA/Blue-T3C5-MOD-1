# #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores..

ano_nasc = 0
ano_atual = 2021
quant_maiores = 0
quant_menores = 0



for p in range( 1, 8) :
        ano_nasc = int(input(f'Ano de nascimento {p}ª pessoa: '))
        idade = ano_atual - ano_nasc
        if idade < 18:
                quant_menores += 1
        else:
                quant_maiores += 1
        
                     
    
print(f'{quant_maiores} são maiores de idade.')
print(f'{quant_menores} são menores de idade.')

