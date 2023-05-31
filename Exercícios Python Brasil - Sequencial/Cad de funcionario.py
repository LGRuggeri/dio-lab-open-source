setor = []
id = []
nome_colaborador = []
funcao = []
idade = []
salario = []
continuar = 's'

while continuar == 's' :
    id.append (input)
    nome_colaborador.append (input('Digite o nome do colaborador: '))
    setor.append (input('Digite o setor: '))
    funcao.append (input('Digite a função: '))
    idade.append (int(input('Digite a idade: ')))
    salario.append (float(input('Digite o salario: ')))
    continuar = (input('Digite \"s\" para continuar: '))
    
for dados_funcionario in range (0,len(id)) :
    print('\nID.......: ',(dados_funcionario+1))
    print('Nome do colaborador.......: ',nome_colaborador[dados_funcionario])
    print('Setor do colaborador.......: ',setor[dados_funcionario])
    print('Função do colaborador......: ',funcao[dados_funcionario])
    print('Idade do colaborador......: ',idade[dados_funcionario])
    print('Salario colaborador......: ',salario[dados_funcionario])
    
     
