# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, 
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade +=1
        return self.idade
    
    def engordar(self, kg):
        self.peso += kg
        return self.peso
    
    def emagrecer(self, kg):
        self.peso -= kg
        return self.peso
    
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05
            return self.altura
        else: 
            return self.altura

nome = input('Digite seu nome: ')
idade = int(input('Qual a sua idade? '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
p1 = Pessoa(nome, idade, peso, altura)
print(vars(p1))
novoPeso = int(input('Digite 1- engordou, 2- emagreceu ou 3- não houve alteração. '))
if novoPeso == 1:
        kg = float(input('Quantos kg você engordou? '))
        novoPeso = p1.engordar(kg)
elif novoPeso == 2:
        kg = float(input('Quantos kg você emagreceu? '))
        novoPeso = p1.emagrecer(kg)
else:
        kg = 0




print(p1.envelhecer()) 
print(p1.crescer())
print(novoPeso)
print(vars(p1))




        
