"""Faça um Programa que peça 2 números inteiros e um número real
A. O produto do dobro do primeiro com metade do segundo .
B. A soma do triplo do primeiro com o terceiro.
C. O terceiro elevado ao cubo."""
from Funcao_dobro_soma_elevado import *


inteiro1= (int(input('Digite o 1 número inteiro:')))
inteiro2= (int(input('Digite o 2 número inteiro:')))
real= (float(input('Digite o 3 número real:')))

print('O produto do dobro do primeiro com metade do segundo',dobro(inteiro1,inteiro2))
print('A soma do triplo do primeiro com o terceiro.',soma(inteiro1,real))
print('O terceiro elevado ao cubo.',elevado(real))