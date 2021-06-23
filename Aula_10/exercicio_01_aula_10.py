# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade

lista_cliente = []
lista_nomes = []
lista_idade = []
lista_composta = []
    
for i in range(4):
    nome = input('Digite seu nome:')
    idade = int(input('Digite a sua idade: '))
    lista_cliente.append(nome)
    lista_cliente.append(idade)    
    i+=1
    lista_composta.append(lista_cliente)
        for i in lista_composta:
            if idade < 18 :
                print(f'{nome} é menor de idade')
            else: 
                print(f'{nome} é maior de idade')
print(lista_cliente)   
        
     
    
