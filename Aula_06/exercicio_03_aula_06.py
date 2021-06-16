# 03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de
# passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de
# acordo com o intervalo passado.

num_inicio = int(input('Digite um número de ínicio: '))
num_fim = int(input('Digite um número de fim: '))
num_intervalo = int(input('Digite um número de intervalo: '))

for i in range(num_inicio, num_fim + 1, num_intervalo):
        print(i)
    