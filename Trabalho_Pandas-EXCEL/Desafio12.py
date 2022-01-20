'''
    Analizando tabela EXCEL
'''

import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_excel('desafio12_A.xlsx')
total = dataframe.shape[0]
quantitativo = dataframe.groupby('Sexo').count()
mediaidade = dataframe['Idade'].mean()
dpidade = dataframe['Idade'].std()
mediamassa = dataframe['Massa'].mean()
dpmassa = dataframe['Massa'].std()
mediaestatura = dataframe['Estatura'].mean()
dpestatura = dataframe['Estatura'].std()
mediaptpre = dataframe.loc[dataframe['Momento'] == 'pre', 'PT'].mean() 
mediaptpos = dataframe.loc[dataframe['Momento'] == 'pos', 'PT'].mean()
desvioptpre = dataframe.loc[dataframe['Momento'] == 'pre', 'PT'].std()
desvioptpos = dataframe.loc[dataframe['Momento'] == 'pos', 'PT'].std()
mediaempre = dataframe.loc[dataframe['Momento'] == 'pre', 'EM'].mean()
mediaempos = dataframe.loc[dataframe['Momento'] == 'pos', 'EM'].mean()
desvioempre = dataframe.loc[dataframe['Momento'] == 'pre', 'EM'].std()
desvioempos = dataframe.loc[dataframe['Momento'] == 'pos', 'EM'].std()
'''existe diferenca significativa no PT após o treino?'''
#plt.scatter(dataframe.loc[dataframe['Momento'] == 'pos', 'PT'], dataframe.loc[dataframe['Momento'] == 'pre', 'PT'])


print('1 - Total de registros: ', total)
print(f'2 - Quantitativo por sexo: {quantitativo["Momento"][1]} Masculino, {quantitativo["Momento"][0]} Feminino')
print(f'3 - Média de idade: {mediaidade:.2f} Desviopadrao: {dpidade:.2f}')
print(f'4 - Média de massa: {mediamassa:.2f} Desviopadrao: {dpmassa:.2f}')
print(f'5 - Média de estrutura: {mediaestatura:.2f} Desviopadrao: {dpestatura:.2f}')
print('-'* 40)
print(f'6A - Média do PT na PRÉ: {mediaptpre:.2f} PÓS: {mediaptpos:.2f}')
print(f'6B - Desvio padrão do PT na PRÉ: {desvioptpre:.2f} PÓS: {desvioptpos:.2f}')
print('7 - Não, pois os dados nao apresentam distribuição normal')
#grafico questao 8
dataframe.hist(column='PT', bins=100, figsize=(10,10))
plt.show()
print(f'10A - Média do EM na PRÉ: {mediaempre:.2f} PÓS: {mediaempos:.2f}')
print(f'10B - Desvio padrão do EM na PRÉ: {desvioempre:.2f} PÓS: {desvioempos:.2f}')
print('11 - Sim os dados apresentao uma distribuicao normal')
#dataframe.hist(column='EM', bins=50, figsize=(10,10))

'''Existe diferença significativa no EM apos o treino? demonstre graficamente'''
