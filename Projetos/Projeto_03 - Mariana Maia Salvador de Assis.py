# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário
# diga que não tem mais ninguém para votar, esse programa precisa ter duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o 
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando 
# um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e 
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização 
# (que virá da função autoriza_voto()) e o voto que é o número que a pessoa votou. 
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, 
# caso o contrário a 2° função deve validar o número que a pessoa escolheu, 
# ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.

votos = []  #Lista para receber os votos dos eleitores

#Função para calcular a idade do eleitor e saber se o mesmo pode votar
def autoriza_voto(anoNasc):
        idade = 2021- anoNasc
        if idade >= 18 and idade <= 70:
                return 'OBRIGATÓRIO'
        elif idade >= 16 and idade >= 70:
                return 'OPCIONAL'
        else: 
            return 'NEGADO'

  
#Função que usa a função autoriza_voto para solicitar o número do candidato
def votacao(autoriza_voto):
                        anoNasc = int(input('Digite o ano do seu nascimento: '))
                        autoriza_voto(anoNasc)
                        if autoriza_voto(anoNasc) == 'OBRIGATÓRIO' or autoriza_voto(anoNasc) == 'OPCIONAL':
                                voto = str(input('Digite o seu voto: 1- Maria, 2- Ana, 3- José, 4- Nulo e 5- Branco ')) #Input do voto
                                votos.append(voto)             #Inclusãode voto na lista votos
                                votosMaria = votos.count('1')  #Contagem no nº 1 na lista
                                votosAna = votos.count('2')    #Contagem no nº 2 na lista
                                votosJose = votos.count('3')   #Contagem no nº 3 na lista
                                votosNulo = votos.count('4')   #Contagem no nº 4 na lista
                                votosBranco = votos.count('5') #Contagem no nº 5 na lista
                                print(votos)
                                #print quantidade de votos cada candidato teve
                                print(f'Quantidade de votos Maria : {votosMaria}, votos Ana : {votosAna}, votos José: {votosJose}, votos nulos : {votosNulo} e votos em branco : {votosBranco}')
                             
                        
                                if votosMaria > votosAna and votosMaria > votosJose:
                                        print(f'Maria foi eleita com {votosMaria} votos!!')
                                elif votosAna > votosMaria and votosAna > votosJose:
                                        print(f'Ana foi eleita com {votosAna} votos!!')
                                elif votosJose > votosMaria and votosJose > votosAna:
                                        print(f'Ana foi eleita com {votosAna} votos!!')   
                        elif autoriza_voto(anoNasc) == 'NEGADO':
                                print('Você não pode votar!')                          

#Loop para inserir votações
while True:
        confereEleitor = input('Eleitor para a votação? [S/N] ').upper() #conferir se tem eleitor para votar
        if confereEleitor in 'SN':
                if confereEleitor == 'S':
                        votacaoT = votacao(autoriza_voto) #chama a função votação                        
                else: 
                        
                        break    # fim do loop
        else: 
                print('Digite S ou N!') #Solicita resposta S ou N


