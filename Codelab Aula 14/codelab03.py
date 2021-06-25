# Faça um programa com uma função chamada somaImposto.
#  A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
#  sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#  A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto, custo):
    precoTotal = custo * taxaImposto
    return precoTotal 
    # print(precoTotal)

valor = float(input('Digite o custo do produto: '))
taxa = float(input('Digite a porcentagem: '))
porcentagem = 1 + taxa/100

preco = somaImposto(valor, porcentagem)

print(preco)
