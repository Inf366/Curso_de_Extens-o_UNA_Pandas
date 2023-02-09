# Autor: GSRS

import pandas as pd
Combus = pd.read_excel("ca-2021-02.xlsx")
#Pega n linhas
#print(Combus.head(5))
#Faz uma análise
#print(Combus.describe())
#Números de linhas e colunas
#print(Combus.shape)
#Pega informação das colunas
#print(Combus.info())

#Pós intervalo

#Linhas específicas
#print(Combus['Revenda'].head(5))
Combus2 = Combus[['Revenda','Municipio','Produto','Valor de Venda']]
#print(Combus2.head(10))
#print(Combus2.loc[3])

#Maior valor
Combus3 = Combus2.loc[Combus2['Produto']=='GASOLINA']
#print(Combus3['Valor de Venda'].max())

print(Combus3[['Revenda','Municipio','Valor de Venda']].max())
