"""Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade
de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as 
informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220."""

valor_hora= (float(input('Digite o valor da sua hora trabalhada: ')))
quantidade_hora_trabalhada= (int(input('Digite a quantidade de horas trabalhadas: ')))

salario= valor_hora * quantidade_hora_trabalhada
if salario <= 900.0:
    desc_sindicato= salario * 0.03
    desc_INSS= salario * 0.10
    desc_FGTS= salario * 0.11
    desconto= desc_sindicato+desc_INSS
    salario_liquido= salario - desconto
elif salario >=900.01 and salario <= 1500.0:
    desc_IR= salario * 0.05
    desc_sindicato= salario * 0.03
    desc_INSS= salario * 0.10
    desc_FGTS= salario * 0.11
    desconto= (desc_sindicato+desc_INSS)+desc_IR
    salario_liquido= salario - desconto
elif salario >=1500.01 and salario <= 2500.0:
    desc_IR= salario * 0.10
    desc_sindicato= salario * 0.03
    desc_INSS= salario * 0.10
    desc_FGTS= salario * 0.11
    desconto= (desc_sindicato+desc_INSS)+desc_IR
    salario_liquido= salario - desconto
else:
    desc_IR= salario * 0.20
    desc_sindicato= salario * 0.03
    desc_INSS= salario * 0.10
    desc_FGTS= salario * 0.11
    desconto= (desc_sindicato+desc_INSS)+desc_IR
    salario_liquido= salario - desconto
    
print(f'O salário bruto é R${salario}, o desconto de IR foi R${desc_IR}, o desconto de INSS foi R${desc_INSS}, o desconto sindicato foi R${desc_sindicato}, o FGTS depositado pela empresa foi R${desc_FGTS},o total de desconto foi R${desconto} o salário liquído é R${salario_liquido}')