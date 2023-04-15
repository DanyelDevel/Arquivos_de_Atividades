#Exemplo 1 - Operações Básicas
'''Faça um programa para a média de um aluno, dadas duas notas'''
'''
nota1 = float(input('Digitea nota 1: '))
nota2 = float(input('Digitea nota 2: '))
media = (nota1+nota2)/2
print(f'A nota do aluno é: {media: .4f}')'''


#exemplo 2 - Estruturas Condicionais
'''Faça um programa para computar a média do aluno e verificar se este aluno efoi aprovado, reprovado ou de recuperação'''
'''
nota1 = float(input('Digitea nota 1: '))
nota2 = float(input('Digitea nota 2: '))
media = (nota1+nota2)/2
print(f'A nota do aluno é: {media: .3f}')

# Reprovado | R | Aprovado
# 0 1 2 3 4 5 6 7 8 9 10
if media >= 7:
    print('Aprovado')

else:
   if media <= 5:
       print('Reprovado')
   else:
       print('Recuperção')'''


#Exemplo 3 - Estruturas de Repetição
'''Faça um programa pára computar a média de N alunos e contar a quantidade de alunos aprovados, reprovados ou recuperação'''
'''
quantidade_alunos = int(input('Digite a  quantidade de alunos: '))

for aluno in range(quantidade_alunos):
    print(f'Digite a nota do aluno {aluno}')
    nota1 = float(input('Digitea nota 1: '))
    nota2 = float(input('Digitea nota 2: '))
    media = (nota1+nota2)/2
    print(f'A nota do aluno é: {media: .2f}')

    #Verificador de aprovação
    # Reprovado | R | Aprovado
    # 0 1 2 3 4 5 6 7 8 9 10
    if media >= 7:
        print('Aprovado')

    else:
        if media <= 5:
        print('Reprovado')
    else:
        print('Recuperção')'''


# Exercicio 4
'''Faça um programa para computar'''
'''
# Recursividade - programa de repetição
def enquanto(n):
    if n >= 0:
        print(n)
        enquanto(n-1)
enquanto(5)'''