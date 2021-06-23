# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.


lista = []
resp = 's'
while resp == 's':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
       print('Esse valor já está na lista!!')
    resp = input('Deseja continuar? [s/n]: ').lower()
    while resp not in ['s','n']:
         resp = input('Resposta inválida, deseja continuar? [s/n]').lower()
print(sorted(lista))
