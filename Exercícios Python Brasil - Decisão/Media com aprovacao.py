"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez"""

nota1_aluno= (int(input('Digite a 1 nota do aluno:')))
nota2_aluno= (int(input('Digite a 2 nota do aluno:')))

media_aluno= (nota1_aluno+nota2_aluno)/2

if media_aluno == 10:
    print('Aluno aprovado com distinção')
elif media_aluno >= 7 and media_aluno < 10:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')