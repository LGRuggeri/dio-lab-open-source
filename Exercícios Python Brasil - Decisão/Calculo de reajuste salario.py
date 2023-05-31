"""As Organizações Tabajara resolveram dar um aumento de salário aos 
seus colaboradores e lhe contraram para desenvolver o programa que 
calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o 
reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser 
realizado, informe na tela:
A.o salário antes do reajuste;
B.o percentual de aumento aplicado;
C.o valor do aumento;
D.o novo salário, após o aumento"""

salario= (float(input('Digite o salário do funcionário:')))

if salario <= 280.0:
    percentual_aumento = 0.20
    reajuste= salario * percentual_aumento
    novo_salario= salario + reajuste
elif salario >= 280.01 and salario <= 700.0:
    percentual_aumento = 0.15
    reajuste= salario * percentual_aumento
    novo_salario= salario + reajuste
elif salario >= 700.01 and salario <= 1500.0:
    percentual_aumento = 0.10
    reajuste= salario * percentual_aumento
    novo_salario= salario + reajuste
else:
    percentual_aumento = 0.05
    reajuste= salario * percentual_aumento
    novo_salario= salario + reajuste
    
print(f'O antigo salário era R${salario}, o aumento percentual foi {percentual_aumento}%, o valor do aumento foi R${reajuste}, o novo salário após aumento é R${novo_salario}')