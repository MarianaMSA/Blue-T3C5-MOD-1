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

# confereEleitor = input('Eleitor para a votação? [S/N]').upper()
# # while confereEleitor == sim:

def autorizaVoto(idade,anoNasc):
        idade = 2021 - anoNasc
        if idade >= 18 and idade <= 70:
                return 'VOTO OBRIGATÓRIO'
        elif idade >=16 and idade >=70:
                return 'VOTO OPCIONAL'
        else: 
            return 'VOTO NEGADO'


def votacao(validacao, voto):
    if autorizaVoto() == 'VOTO NEGADO':
            return 'Você não pode votar'
    else:
        return votoEleitor



nasc = int(input('Digite o ano do seu nascimento: '))
validacao = autorizaVoto(0,nasc)
print (validacao)


def votacao(validacao, voto):
    if autorizaVoto() == 'VOTO NEGADO':
            return 'Você não pode votar'
    else:
        return votoEleitor

votoEleitor = int(input('Diigite o seu voto: '))
votacao(validacao)
        