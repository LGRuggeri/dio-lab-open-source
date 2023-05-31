"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""

produto= (float(input('Digite o preço do 1 produto:')))
produto1= (float(input('Digite o preço do 2 produto:')))
produto2= (float(input('Digite o preço do 3 produto:')))

if produto < produto1 and produto < produto2:
    print(f'O produto com o menor preço é o 1: {produto}')
elif produto1 < produto and produto1 < produto2:
    print(f'O produto com o menro preço é o 2: {produto1}')
else:
    print(f'O produto com o menro preço é o 3: {produto2}')