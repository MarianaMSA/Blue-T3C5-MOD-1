# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)
n = 0
quant_n = 0
soma = 0
quant_n = int(input('Digite a quantidade de números: '))

for i in range(quant_n):
    n = int(input('Digite um número : '))
    if i < quant_n:
        soma += n
print(soma)
       
