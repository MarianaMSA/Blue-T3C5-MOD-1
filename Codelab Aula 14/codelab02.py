#  Faça um programa, com uma função que necessite de um argumento. 
#  A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, 
#  se seu argumento for negativo e ‘0’ se for 0.

def fun (num):
        if num > 0 :
           return 'P'
        if num < 0  :
           return 'N'
        else: 
            return '0'
    

numero = int(input('Digite um valor: '))
resultado = fun(numero)
print(resultado)