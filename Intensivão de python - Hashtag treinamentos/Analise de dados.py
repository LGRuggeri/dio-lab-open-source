import pandas as pd
import plotly.express as px

#Passo 1: importar a base de dados
tabela= pd.read_csv(r'C:\Users\Gustavo\Desktop\Intensivão de PYTHON - HASHTAG\AULA 2\clientes.csv', sep= ';',encoding= 'latin')


# deletar coluna inútil
tabela= tabela.drop('Unnamed: 8',axis=1) 
print(tabela)


#Passo 2: Visualizar a base de dados
    #Entender as informações que você tem disponíveis
    #Procurar os erros na base de dados
print(tabela.info())    

    
#Passo 3: Tratamento dos dados
    #Valores no formato errado
tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce')
    
    #Valores vazios
tabela= tabela.dropna()
    

#Passo 4:Análise inicial = entender como estão as notas dos clientes
print(tabela.describe())


#Passo 5:Análise completa = traçar o perfil ideal de cliente, entender como cada característica do cliente empacta na nota
    #Cria o gráfico
for colunas in tabela.columns:    
    grafico= px.histogram(tabela, x=colunas,y='Nota (1-100)', histfunc='avg', text_auto=True, nbins=10)

    #exibe o gráfico
    grafico.show()