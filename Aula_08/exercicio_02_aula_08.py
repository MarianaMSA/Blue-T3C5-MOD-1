# 2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

respostas = []
print('Responder Sim ou Nao')

resposta = input('Telefonou para a vítima? ').lower()

if resposta == 'sim' or resposta == 'nao':
        respostas.append(resposta)
        resposta = input('Esteve no local do crime? ').lower()
        respostas.append(resposta)
        resposta = input('Mora perto da vítima? ').lower()
        respostas.append(resposta)
        resposta = input('Devia para a vítima? ').lower()
        respostas.append(resposta)
        resposta = input('Já trabalhou com a vítima? ').lower()
        respostas.append(resposta)
        
total_sim = int(respostas.count('sim'))

if total_sim == 5 :
    print('Assasino!')
elif total_sim == 3 or total_sim == 4 :
    print('Cúmplice!')
elif total_sim == 2 :
    print('Suspeito!')
else:
    print('Inocente!')
        


