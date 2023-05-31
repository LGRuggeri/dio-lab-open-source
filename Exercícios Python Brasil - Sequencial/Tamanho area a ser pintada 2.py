"""Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros 
quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou 
em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:
A. comprar apenas latas de 18 litros;
B. comprar apenas galões de 3,6 litros;
C. misturar latas e galões, de forma que o desperdício de tinta seja 
menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias."""
import math

area_pintura= (int(input('Digite o tamanho da area total a ser pintada:')))

area_cobertura_lata= math.ceil((area_pintura/6)/18)
valor_compra_lata= area_cobertura_lata*80
print(f'A quantidade de lata a ser comprada é: {area_cobertura_lata}',
      f'\nE o valor da compra é: {valor_compra_lata}')

print('#############################################################')

area_cobertura_galao= math.ceil((area_pintura/6)/3.5)
valor_compra_galao= area_cobertura_galao*25
print(f'A quantidade de galões a ser comprado é: {area_cobertura_galao}',
      f'\nE o valor da compra é: {valor_compra_galao}')

print('#############################################################')

area_cobertura_lata= math.ceil(((area_pintura/6)/18) * 1.1)
if area_cobertura_lata != 0:
      area_cobertura_galao= math.ceil(((area_cobertura_lata/6)/3.5) * 1.1)
      valor_compra_lata_galao = round((area_cobertura_lata*25)+(area_cobertura_galao*80))
      lata_menos_galao= math.ceil(area_cobertura_lata - area_cobertura_galao)
      print(f'Para ter um menor desperdício de tinta pode ser usada {area_cobertura_galao} de tinta',
            f'\nmais {lata_menos_galao} galões',
            f'\nDando o valor total de: R${valor_compra_lata_galao}')
     
     