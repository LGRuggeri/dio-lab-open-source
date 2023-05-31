#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura= (float(input('Digite a sua altura em centímetros:')))
print('Vamos calcular o seu IMC')

altura = altura/100
imc= (72.7*altura)-58

print(f'Seu peso ideal é: {imc}')