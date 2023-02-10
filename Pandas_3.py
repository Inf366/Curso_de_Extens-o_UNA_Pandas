# Autor: GSRS

import pandas as pd
import numpy as np

Combus = pd.read_excel('ca-2021-02.xlsx')
Hab = pd.read_csv('ibge_num_habitantes_estimado.csv',sep=";")
Hab.rename(columns={"Estado":"Estado - Sigla"}, inplace=True)

#Combus['Ativo'] = True
#print(Combus)
# Coluna Obs para Melhor Cidade
#Combusobs = Combus['Obs'] = ["Melhor Cidade" if municipio == 'BELO HORIZONTE' else None for municipio in Combus['Municipio']]
#print(Combusobs.loc[Combusobs['Municipio'].isin(['BELO HORIXONTE','SAO PAULO','CAMPINAS']),['Municipio','Obs']])
Combus['Status Preço'] = np.where(Combus['Valor de Venda']>6.5,'Caro','Barato')

#Pós Intervalo

#Posto de Gasolina por habitante
#Cria um Merge nos dois DataFrames
colunas = ['Municipio','Estado - Sigla']
Combus_merge = Combus.merge(Hab,how="inner",on=colunas)

#Destroi colunas nulas (N/A)
Combus_merge.dropna(axis='columns',inplace=True)

colunas =['Regiao - Sigla','Nome da Rua','Numero Rua',
         'Bairro','Cep','Produto','Data da Coleta',
         'Valor de Venda','Unidade de Medida','Bandeira','Status Preço']

Combus_merge.drop(labels=colunas, axis=1,inplace=True)

#Remove as linhas duplicadas
Combus_merge.drop_duplicates(inplace=True)

#Agrupar e contar quantos postos tem na cidade
Combus_por_muni = Combus_merge.groupby(by=['Estado - Sigla','Municipio','NumHabitantes2021']).count()
Combus_por_muni.reset_index(inplace=True)
Combus_por_muni.drop('CNPJ da Revenda',axis=1,inplace=True)
Combus_por_muni.rename(columns={'Revenda':'Numero de Postos'},inplace=True)
#
Combus_por_muni['PostosPorHabitante'] = (Combus_por_muni["Numero de Postos"]/Combus_por_muni["NumHabitantes2021"])

print(Combus_por_muni)
print(Combus_por_muni.info())
