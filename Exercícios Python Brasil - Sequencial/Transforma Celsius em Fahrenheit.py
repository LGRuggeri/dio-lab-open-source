#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_Celsius= (float(input('Digite a temperatura Fahrenheit a ser convertida para Celsius:')))

temperatura_Fahrenheit = round((temperatura_Celsius*1.8)+32)

print(f'A temperatura em Fahrenheit é: {temperatura_Fahrenheit}')