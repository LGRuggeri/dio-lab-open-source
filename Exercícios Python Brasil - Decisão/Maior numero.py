#Faça um Programa que leia três números e mostre o maior deles.


num= (int(input('Digite o 1 número:')))
num1= (int(input('Digite o 2 número:')))
num2= (int(input('Digite o 3 número:')))

if num > num1 and num > num2:
    print(f'O maior número foi o 1 número: {num}')
elif num1 > num and num1 > num2:
    print(f'O maior número foi o 2 número: {num1}')
else:
    print(f'O maior número foi o 3 número: {num2}')