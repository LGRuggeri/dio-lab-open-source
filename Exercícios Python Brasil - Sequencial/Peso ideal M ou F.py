#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura= (float(input('Digite a sua altura em centímetros:')))
sexo= (input('\nDigite o seu sexo (M)Masculino ou (F)Feminino:'))
print('Vamos calcular o seu IMC')

if sexo == 'M' or sexo == 'm':
    altura = altura/100
    imc= round((72.7*altura) - 58)
else:
    altura = altura/100
    imc= round((62.1*altura) - 44.7)
    
print(f'Seu peso ideal é: {imc}')

