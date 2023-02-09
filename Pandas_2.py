# Autor: GSRS

import pandas as pd
Combus = pd.read_excel("C:\\Users\\Guilherme Souza\\Desktop\\Pandas_Una\\ca-2021-02.xlsx")
Combus2 = Combus[['Revenda','Municipio','Produto','Valor de Venda']]
Combusgas = Combus2.loc[Combus2['Produto']=='GASOLINA']

#print(Combusgas[['Revenda','Municipio','Valor de Venda']].max())
Combusbh = Combus2.loc[(Combus2['Produto']=='ETANOL') & (Combus2['Municipio'] == 'BELO HORIZONTE')]


#Ordenar com o sort
#Combusbh.sort_values(by='Valor de Venda',inplace=True)
#print(Combusbh)

#Gasolina e Gasolina Aditivada no bairro BELA VISTA em SÃO PAULO
#print(Combus.loc[(Combus['Bairro']=='MOOCA')&(Combus['Municipio'] == 'SAO PAULO')&((Combus['Produto']=='GASOLINA')|(Combus['Produto']=='GASOLINA ADITIVADA')),['Valor de Venda']].mean())

#Pós intervalo

#Média de valor de venda em todo o Brasil usando groupby
Media_por_Combus = Combus[['Produto','Valor de Venda']].groupby(by='Produto').mean().round(2)
#print(Media_por_Combus)

#Adicionar coluna booleana chamada "Ativo" que será True para todas as linhas
#Combus["Ativo"] = True
#print(Combus.info())

#Coluna nova chamada "Obs" que preencha automaticamente MELHOR CIDADE"
#Quando o município for Belo Horizonte...
#Amanhã
#Combus["Obs"] = "Melhor Cidade" 
#print(Combus)

#Exportar as médias de combustíveis usando toExcel
Media_por_Combus.to_excel("Médias_Combustíveis_Brasil.xlsx",sheet_name='Médiano Brasil')
print(Media_por_Combus)
print("Fim")
