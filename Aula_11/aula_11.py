# contatosLista = [('Ana', '1234-1234'), ('Mariana', '1234-1234'), ('Marina', '1234-1234'), ('Rafael', '1234-1234'), ('Joao', '1234-1234')]
# print(contatosLista)
# print(type(contatosLista))


# contatos = dict(contatosLista)
# print(contatos)
# print(type(contatos))
# print(contatos['Mariana'])

# print()
# nome = input('Digite um nome:')
# print(contatos.get(nome, 'Desulpe, esse nome não está no sistema'))
# vingadores = {'Chris Evans' :'Capitão América', 'Mark Ruffalo': 'Hulk', 
# 'Tom Hiddleston' : 'Loki', 'Chris Hemworth': 'Thor', 'Robert Downey Jr' : 'Homem de Ferro',
# 'Scarlett Johansson': 'Viúva Negra'}

# print('Hulk' in vingadores.values()) ##valor sempre booleano

# vingadores ['Mariana'] = 'Oi'
# print(vingadores)
# print(sorted(vingadores.keys()))
# print(sorted(vingadores.values()))

# Incluir
# nome = input('Digite nome:')
# personagem = input('Digite personagem:')
# vingadores [nome] = personagem

# Deletar
# print(vingadores)
# del vingadores['Mariana']
# print(vingadores)

# 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9
#  (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados
#   desses números.

# lista = [1, 4, 5, 6, 7, 9]
# n_quadrados = dict()

# for n in lista:
#     n_quadrados [n] = n ** 2
#     print(n_quadrados)

# b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10]
#  e cada valor associado é o número ao quadrado.​

# quadrados = {}

# for n in range (1,11):
#     quadrados[n] = n ** 2
#     print(quadrados)

### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos =  { 'Abacate': '05', 'Abacaxi': '03', 'Banana': '08' }
n = 0 
compra = print(input('O que você quer comprar ?'))
quantidade = print(input('O que você quer comprar ?'))
produtos [compra] = quantidade

if 