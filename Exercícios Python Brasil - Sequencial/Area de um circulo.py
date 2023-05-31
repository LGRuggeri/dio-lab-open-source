#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio_do_circulo= (float(input('Digite o raio do círculo:')))

area_do_circulo = (raio_do_circulo**2)*math.pi
area_do_circulo = round(area_do_circulo,2)
print(f'A área do círculo é: {area_do_circulo}')