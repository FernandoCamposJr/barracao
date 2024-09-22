## calcular o desvio padrão:

import pandas as pd

# Caminho completo para o arquivo CSV
file_path = r'C:\Users\ferna\OneDrive\Área de Trabalho\CSV Pycharm\tabela-analise-barracao.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';')

# Calcular o desvio padrão das colunas especificadas
colunas_interesse = ['NofClx', 'medianKHz', 'avSPL', 'TrDur_us', 'midpointICI']
desvios = df[colunas_interesse].std()

# Exibir o desvio padrão das colunas selecionadas
print("Desvio padrão das colunas selecionadas:")
print(desvios)













