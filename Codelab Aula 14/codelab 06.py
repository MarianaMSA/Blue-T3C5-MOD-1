# Escreva uma função que, dado um número nota representando a nota de um estudante,
# converte o valor de nota para um conceito (A, B, C, D, E e F).


# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.9	F

def  notaConceito (nota):
    if nota >= 9.0:
        return 'A'
    elif nota >= 8.0:
        return 'B'
    elif nota >= 7.0:
        return 'C'
    elif nota >= 6.0:
        return 'D'
    elif nota <= 4.9:
        return 'E'

notaAluno = float(input('Digite a nota do Aluno: '))
notaConceito(notaAluno)
conceito = notaConceito(notaAluno)
print(f'O conceito do aluno foi: {conceito}')