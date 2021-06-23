# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes 
# informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]

print(len(L))
print(max(L))
print(min(L))
print(sum(L))
L.sort()
print("A lista em ordem crescente é",L)
L.reverse()
print("A lista em ordem decrescente é",L)


