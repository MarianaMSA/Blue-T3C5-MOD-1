# 3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random


lista_forca = ['Banana', 'Abacate', 'Manga', 'Kiwi', 'Tomate', 'Cenoura', 'Alface', 'Cebola', 'Alho', ]

palavra_sorteada = random.choice(lista_forca)

for i in range(palavra_sorteada) :
        letra_jogador = input('Digite uma letra: ')
        while i <= 6 :
            if letra_jogador != palavra_sorteada :
                print(f'Tentativa {i}, tente mais uma vez!')
            elif letra_jogador == palavra_sorteada :
                print('Você acertou!!!')


