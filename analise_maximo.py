## calcular o valor máximo:
import pandas as pd

# Caminho completo para o arquivo CSV
file_path = r'C:\Users\ferna\OneDrive\Área de Trabalho\CSV Pycharm\tabela-analise-barracao.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';')

# Calcular o valor máximo das colunas especificadas
colunas_interesse = ['NofClx', 'medianKHz', 'avSPL', 'TrDur_us', 'midpointICI']
maximos = df[colunas_interesse].max()

# Exibir o valor máximo das colunas selecionadas
print("Valor máximo das colunas selecionadas:")
print(maximos)