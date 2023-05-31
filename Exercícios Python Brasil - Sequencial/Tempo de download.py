"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
usando este link (em minutos)."""

import datetime

tamanho_arquivo_download= (float(input('Digite o tamanho do arquivo em MB para dowload:')))
velocidade_internet= (int(input('Digite a velocidade da internet em Mbps:')))

tempo_de_download= int(tamanho_arquivo_download//velocidade_internet)

print('O tempo necessário para download em minutos é:',datetime.time(tempo_de_download),'min')