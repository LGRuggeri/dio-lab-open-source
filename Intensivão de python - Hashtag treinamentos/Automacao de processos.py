import pyautogui as pgi
import time
import pandas as pd
import pyperclip as pcp

#Passo 1: Acessar o sistema da empresa
time.sleep(1)
pgi.click(x=229, y=748)
pgi.hotkey('ctrl','t')
time.sleep(1)
pgi.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
time.sleep(1)
pgi.press('enter')

#Passo 2: Fazer login no sistema
time.sleep(3)
pgi.click(x=634, y=369)
pgi.write('luiz.ruggeri')
time.sleep(2)
pgi.click(x=584, y=459)
pgi.write('45620')
time.sleep(2)
pgi.click(x=620, y=532)
time.sleep(4)

#Passo 3: Baixar a base de dados
pgi.click(x=477, y=356)
pgi.click(x=555, y=195)
time.sleep(3)

#Passo 4: Calcular indicadores
tabela = pd.read_csv(r'C:\Users\Gustavo\Desktop\Intensivão de PYTHON - HASHTAG\AULA 1\Compras.csv', sep=';')

#Total gasto
total_gasto= tabela['ValorFinal'].sum()

#quantidade
quantidade= tabela['Quantidade'].sum()

#preço medio
preco_medio= total_gasto/quantidade

#Passo 5: Enviar e-mail para diretoria
#Acessar e-mail
time.sleep(3)
pgi.hotkey('ctrl','t')
time.sleep(1)
pgi.write('https://mail.google.com/mail/u/0/#inbox')
time.sleep(1)
pgi.press('enter')

#Escrever o e-mail
time.sleep(4)
pgi.click(x=132, y=209)
time.sleep(2)
pgi.click(x=1255, y=306)
time.sleep(2)
pgi.write('lgcruggeri@gmail.com')
time.sleep(2)
pgi.press('tab')
time.sleep(2)
pgi.press('tab')
pcp.copy('Relatório de compras')
pgi.hotkey('ctrl','v')
time.sleep(2)
pgi.press('tab')
texto= f"""
Prezados,
Segue em anexo o relatório de compras

Total Gasto: R${total_gasto: ,.2f}
Quantidade de Produtos: {quantidade: ,}
Preço Médio: R${preco_medio: ,.2f}     

Dúvidas fico à disposição.
Att.,
Luiz Ruggeri"""
pcp.copy(texto)
pgi.hotkey('ctrl','v')

#Envia o e-mail
time.sleep(2)
pgi.hotkey('ctrl', 'enter')
time.sleep(2)
pgi.click(x=768, y=202)