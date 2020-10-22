
#Bibliotecas utilizadas para analise dos dados
import pandas as pd 
import numpy as np
import math
import json

#dicionario criado para conter respostas e dados importantes que vao para o relatorio no final
respostas_v6 = {}
respostas_v7 = {}

#variavel para focar em V6 primeiro e depois em V7
variavel = "V6"

#Leitura e manipulacao de dados no arquivo csv
df = pd.read_csv("./Pedro Henrique Fabriz Ulhoa - dados.csv")
df = df[['ID', 'V1', 'V6', 'V7']]

#agora para V6
#calculos gerais
respostas_v6['numero de amostras totais'] = len(df['V6'])
respostas_v6['numero de classes'] = math.ceil(math.sqrt(len(df['V6'])))
respostas_v6['passo do intervalo'] = round((max(df['V6']) - min(df['V6']))/respostas_v6['numero de classes'], 1) #arredondar para 1 casa decimal
respostas_v6['valor maximo na amostra'] = max(df['V6'])
respostas_v6['valor minimo na amostra'] = min(df['V6'])
respostas_v6['freq 4,9 |- 5,1'] = len(df[(df['V6'] >= 4.9) & (df['V6'] < 5.1)])
respostas_v6['freq 5,1 |- 5,3'] = len(df[(df['V6'] >= 5.1) & (df['V6'] < 5.3)])
respostas_v6['freq 5,3 |- 5,5'] = len(df[(df['V6'] >= 5.3) & (df['V6'] < 5.5)])
respostas_v6['freq 5,5 |- 5,7'] = len(df[(df['V6'] >= 5.5) & (df['V6'] < 5.7)])
respostas_v6['freq 5,7 |- 5,9'] = len(df[(df['V6'] >= 5.7) & (df['V6'] < 5.9)])
respostas_v6['freq 5,9 |- 6,1'] = len(df[(df['V6'] >= 5.9) & (df['V6'] < 6.1)])
respostas_v6['freq 6,1 |- 6,3'] = len(df[(df['V6'] >= 6.1) & (df['V6'] < 6.3)])
respostas_v6['freq 6,3 |- 6,5'] = len(df[(df['V6'] >= 6.3) & (df['V6'] < 6.5)])
respostas_v6['freq 6,5 |- 6,8'] = len(df[(df['V6'] >= 6.5) & (df['V6'] < 6.8)])
#calculo frequencia relativa
respostas_v6['freq rel 4,9 |- 5,1'] = round(respostas_v6['freq 4,9 |- 5,1'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 5,1 |- 5,3'] = round(respostas_v6['freq 5,1 |- 5,3'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 5,3 |- 5,5'] = round(respostas_v6['freq 5,3 |- 5,5'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 5,5 |- 5,7'] = round(respostas_v6['freq 5,5 |- 5,7'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 5,7 |- 5,9'] = round(respostas_v6['freq 5,7 |- 5,9'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 5,9 |- 6,1'] = round(respostas_v6['freq 5,9 |- 6,1'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 6,1 |- 6,3'] = round(respostas_v6['freq 6,1 |- 6,3'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 6,3 |- 6,5'] = round(respostas_v6['freq 6,3 |- 6,5'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)
respostas_v6['freq rel 6,5 |- 6,8'] = round(respostas_v6['freq 6,5 |- 6,8'] / float(respostas_v6['numero de amostras totais']) * 100 , 2)

#Agora para V7
#Calculos gerais
respostas_v7['numero de classes'] = math.ceil(math.sqrt(len(df['V7'])))
respostas_v7['numero de amostras totais'] = len(df['V7'])
respostas_v7['passo do intervalo'] = round((max(df['V7']) - min(df['V7']))/respostas_v7['numero de classes'], 1) #arredondar para 1 casa decimal
respostas_v7['valor maximo na amostra'] = max(df['V7'])
respostas_v7['valor minimo na amostra'] = min(df['V7'])
respostas_v7['freq 3,7 |- 3,9'] = len(df[(df['V7'] >= 3.7) & (df['V7'] < 3.9)])
respostas_v7['freq 3,9 |- 4,1'] = len(df[(df['V7'] >= 3.9) & (df['V7'] < 4.1)])
respostas_v7['freq 4,1 |- 4,3'] = len(df[(df['V7'] >= 4.1) & (df['V7'] < 4.3)])
respostas_v7['freq 4,3 |- 4,5'] = len(df[(df['V7'] >= 4.3) & (df['V7'] < 4.5)])
respostas_v7['freq 4,5 |- 4,7'] = len(df[(df['V7'] >= 4.5) & (df['V7'] < 4.7)])
respostas_v7['freq 4,7 |- 4,9'] = len(df[(df['V7'] >= 4.7) & (df['V7'] < 4.9)])
respostas_v7['freq 4,9 |- 5,1'] = len(df[(df['V7'] >= 4.9) & (df['V7'] < 5.1)])
respostas_v7['freq 5,1 |- 5,3'] = len(df[(df['V7'] >= 5.1) & (df['V7'] < 5.3)])
respostas_v7['freq 5,3 |- 5,5'] = len(df[(df['V7'] >= 5.3) & (df['V7'] < 5.5)])
respostas_v7['freq 5,5 |- 5,7'] = len(df[(df['V7'] >= 5.5) & (df['V7'] < 5.7)])
#calculo da frequencia relativa
respostas_v7['freq 3,7 rel |- 3,9'] = round(respostas_v7['freq 3,7 |- 3,9'] / float(respostas_v7['numero de amostras totais']) * 100 , 2)
respostas_v7['freq 3,9 rel |- 4,1'] = round(respostas_v7['freq 3,9 |- 4,1'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 4,1 rel |- 4,3'] = round(respostas_v7['freq 4,1 |- 4,3'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 4,3 rel |- 4,5'] = round(respostas_v7['freq 4,3 |- 4,5'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 4,5 rel |- 4,7'] = round(respostas_v7['freq 4,5 |- 4,7'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 4,7 rel |- 4,9'] = round(respostas_v7['freq 4,7 |- 4,9'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 4,9 rel |- 5,1'] = round(respostas_v7['freq 4,9 |- 5,1'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 5,1 rel |- 5,3'] = round(respostas_v7['freq 5,1 |- 5,3'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 5,3 rel |- 5,5'] = round(respostas_v7['freq 5,3 |- 5,5'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 
respostas_v7['freq 5,5 rel |- 5,7'] = round(respostas_v7['freq 5,5 |- 5,7'] / float(respostas_v7['numero de amostras totais']) * 100 , 2) 

print(df)
print(respostas_v7)

with open('r_v6.json', 'w') as json_file:
    json.dump(respostas_v6, json_file)
with open('r_v7.json', 'w') as json_file:
    json.dump(respostas_v7, json_file)


print(respostas_v6['freq 6,5 |- 6,8']) / 78.0
# freq_table_V6 = pd.DataFrame(data = {'V6(faixa)': ["freq 3,7 |- 3,9","freq 3,9 |- 4,1"]})
# print(freq_table_V6)