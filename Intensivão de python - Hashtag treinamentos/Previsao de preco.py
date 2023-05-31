import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


#importando a tabela
tabela= pd.read_csv(r'C:\Users\Gustavo\Desktop\Intensivão de PYTHON - HASHTAG\AULA 4\barcos_ref.csv')
print(tabela)

#Verificando qual a informação de maior relevância
print(tabela.corr()[['Preco']])
sns.heatmap(tabela.corr()[['Preco']], annot=True, cmap='Blues')
plt.show()

#Criando o modelo 
y= tabela['Preco']
x= tabela.drop('Preco', axis=1)
x_treino, x_teste, y_treino, y_teste= train_test_split(x,y, test_size=0.3, random_state=1)

#Cria as inteligencias artificiais
modelo_regressaolinear= LinearRegression()
modelo_arvoredecisao= RandomForestRegressor()

#Treina as inteligencias artificiais
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

#Criar as previsões
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

#Comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

#Análise gráfica
tabela_auxiliar= pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsoes ArvoreDeDecisao'] = previsao_arvoredecisao
tabela_auxiliar['Previsoes RegressaoLinear'] = previsao_regressaolinear

#plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

#Importando nova tabela e verificando o barco de maior valor

nova_tabela= pd.read_csv(r'C:\Users\Gustavo\Desktop\Intensivão de PYTHON - HASHTAG\AULA 4\novos_barcos.csv')
print(nova_tabela)
previsao= modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

