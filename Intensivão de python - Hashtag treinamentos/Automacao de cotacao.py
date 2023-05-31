from selenium import webdriver as wd
import pandas as pd

#Abre o navegador 
nav= wd.Chrome()
nav.get('https://google.com.br')

#Importação tabela
tabela= pd.read_excel(r'C:\Users\Gustavo\Desktop\Intensivão de PYTHON - HASHTAG\AULA 3\commodities.xlsx')
print(tabela)

#Pega as cotações dos produtos no site e informa na planilha
for linha in tabela.index:
    produto= tabela.loc[linha, 'Produto']
    produto= produto.replace('ã','a').replace('ç','c').replace('á','a').replace(
    'ó','o').replace('ú','u').replace('é','e')
    link= f'https://www.melhorcambio.com/{produto.lower()}-hoje'
    print(link)
    nav.get(link)
    preco= nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco= preco.replace('.','').replace(',','.')
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)
    
print(tabela)

#Preenche e gera uma planilha atualizada   
nav.quit()
tabela['Comprar'] = tabela['Preço Ideal'] > tabela['Preço Atual']
tabela.to_excel('commodities_atualizado.xlsx', index=False)    

