# Projeto 02 – Jogo Jokenpô
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue 
# pedra, papel e tesoura (Jokenpô) com você. O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um 
# (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade
#  de rodadas, se não finalize o programa.
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 11.

from random import randint

jogar = 's'
cont_jogador = 0
cont_computador = 0
empate = 0
nJogadas = 0
jogosTotal = []
nJogadas = int(input('Quantas vezes você quer jogar?'))

for i in range (nJogadas):
        while i <= nJogadas : 
            computador = randint(0, 2) #sorteio do palpite do computador
            jogador = 0
            jogo = ('Pedra', 'Papel', 'Tesoura')
            lista = [0, 1, 2]
            jogador = int(input('Escolha a sua jogada: [0] Pedra, [1] Papel e [2] Tesoura  '))
            while jogador not in lista:
                    jogador = int(input('Digite um valor válido [0, 1 ou 2]. Qual é a sua jogada? '))
            print(f'Computador jogou {jogo[computador]}.')## Jogo puxa a string relativa ao numero da lista
            print(f'Jogador jogou {jogo[jogador]}.')

            if computador == 0:
                if jogador == 0:
                    empate += 1
                elif jogador == 1:
                    cont_jogador += 1
                elif jogador == 2:
                    cont_computador += 1

            elif computador == 1:
                if jogador == 0:
                    cont_computador += 1
                elif jogador == 1:
                    empate += 1
                elif jogador == 2:
                    cont_jogador += 1

            elif computador == 2:
                if jogador == 0:
                    cont_jogador += 1
                elif jogador == 1:
                    cont_computador += 1
                elif jogador == 2:
                    empate += 1
            if i <= nJogadas:
                break
            print(f'Pontuação : Jogador {cont_jogador} Computador {cont_computador} Empate {empate}')   
            
else:
    if cont_jogador > cont_computador:
        print(f'Você venceu o computador por {cont_jogador} a {cont_computador}.')
    elif cont_jogador < cont_computador:
        print(f'O computador venceu você por {cont_computador} a {cont_jogador}.')
    elif cont_jogador == cont_computador:
        print(f'Empate.')
    jogar = str(input('Deseja continuar a jogar? ''[S/N] ')).lower()
    while jogar not in 'sn':
        jogar = str(input('Digite um dado válido. Deseja continuar a jogar? [S/N] ')).lower()        