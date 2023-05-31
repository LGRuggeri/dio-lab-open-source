import datetime

d1 = []
d2 = datetime.date.today
id_item = []
id_item_dep = []
id_grupo = []
nome_grupo = []
id_subgrupo = []
nome_subgrupo = []
nome_item = []
departamento = []
valor_item = []
cadastro_equipamento = 's'
depreciacao = 's'
depreciar = 's'
valor_depreciado = 0



while cadastro_equipamento == 's':
    id_item.append (int)
    nome_item.append (input('Digite o nome do item a ser cadastrado: '))
    valor_item.append (float(input('Digite o valor do item: ')))
    d1.append (input('Digite a data da compraDeskJet Ink Advantage 3776: '))
    departamento.append (input('Digite a qual departamento pertence o item: '))
    id_grupo.append (int(input('Digite o cód.grupo: ')))
    nome_grupo.append (input('Digite o nome do grupo: '))
    id_subgrupo.append (int(input('Digite o Sub-grupo do item: ')))
    nome_subgrupo.append (input('Digite o nome do Sub-grupo do item: '))
    cadastro_equipamento = input ('Digite "s" para continuar cadastro: ')
    
for valor_origem in range (0,len(id_item)):
    print('\nID item.......: ',(valor_origem+1))
    print('Nome do item.......: ',nome_item[valor_origem])
    print('Valor do item.......: ',valor_item[valor_origem])
    print('Data da compra do item.......: ',d1[valor_origem])
    print('Departamento.......: ',departamento[valor_origem])
    print('ID grupo do item.......: ',id_grupo[valor_origem])
    print('Nome do grupo......: ',nome_grupo[valor_origem])
    print('ID sub-grupo do item......: ',id_subgrupo[valor_origem])
    print('Nome do sub-grupo do item......: ',nome_subgrupo[valor_origem])
    
    depreciar = input ('Digite você gostaria de realizar a depreciação de algum item: ')
    if depreciar == 's':
        while depreciacao == 's':
            id_item_dep = (int(input('Digite o ID do item: ')))
            if d1 != d2 :
                print("O valor do item antes da depreciação era: ",valor_item[valor_origem])
                valor_depreciado = valor_item[valor_origem] * 0.1
                print("O valor depreciado do item foi: ",valor_depreciado)
                novo_valor_item = valor_item[valor_origem] - valor_depreciado
                print("O novo valor do item é: ",novo_valor_item)
            elif d1 == d2:
             print('O tempo de compra do item não atende o perído para depreciação. ')
            else:
                ('Digite valor não correspondente!!')
                
            depreciacao = input('Digite "s" para continuar cadastro: ')
            