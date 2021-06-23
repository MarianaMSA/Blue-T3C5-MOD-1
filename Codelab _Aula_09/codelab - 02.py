# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.


lista = []
lista_par = []
lista_impar = []

resp = 's'

while resp == 's':

    valor = int(input('Digite um valor: '))
    lista.append(valor)

    resp = input('Deseja continuar? [s/n]: ').lower()

    while resp not in ['s','n']:
        resp = input('Resposta inválida, deseja continuar? [s/n]').lower()

for i in lista:
    
        if i %2 == 0 :
           lista_par.append(i) 
        else:
            lista_impar.append(i) 
print(lista)
print(lista_par)
print(lista_impar)


# lista = []
# pares = []
# impares = []

# valor = int(input("Digite um número: "))
# lista.append(valor)

# while True:
#     resposta = input("Deseja adicionar outro número? (S/N): ").lower()
#     while resposta != "s" and resposta != "n":
#         resposta = input("Erro! Deseja adicionar outro número? (S/N): ").lower()
    
#     if resposta == "s":
#         valor = int(input("Digite outro número: "))
#         lista.append(valor)
#     if resposta == "n":
#         break

# for x in lista:
#     if x % 2 == 0:
#         pares.append(x)
#     else:
#         impares.append(x)

# print(f"Lista completa: {lista}")
# print(f"Lista de pares: {pares}")
# print(f"Lista de ímpares: {impares}")
