# 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
# quantas vezes aparece as vogais a,e,i,o,u


frase_usuario = input('Digite uma frase: ').lower()
total_vogais = 0


for i in frase_usuario:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
       total_vogais += 1
###print('Quantidade de vogais:', total_vogais)



    

       
        

   