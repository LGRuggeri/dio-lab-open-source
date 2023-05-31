#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperatura_Fahrenheit= (float(input('Digite a temperatura Fahrenheit a ser convertida para Celsius:')))

temperatura_Celsius = round(5*((temperatura_Fahrenheit-32)/9))

print(f'A temperatura em Celsius é: {temperatura_Celsius}')