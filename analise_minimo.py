## calcular o valor mínimo:

import pandas as pd

# Caminho completo para o arquivo CSV
file_path = r'C:\Users\ferna\OneDrive\Área de Trabalho\CSV Pycharm\tabela-analise-barracao.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';')

# Calcular o valor mínimo das colunas especificadas
colunas_interesse = ['NofClx', 'medianKHz', 'avSPL', 'TrDur_us', 'midpointICI']
minimos = df[colunas_interesse].min()

# Exibir o valor mínimo das colunas selecionadas
print("Valor mínimo das colunas selecionadas:")
print(minimos)