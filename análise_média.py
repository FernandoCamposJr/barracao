import pandas as pd

# Caminho completo para o arquivo CSV
file_path = r'C:\Users\ferna\OneDrive\Área de Trabalho\CSV Pycharm\tabela-analise-barracao.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';')

# Calcular a média das colunas especificadas
colunas_interesse = ['NofClx', 'medianKHz', 'avSPL', 'TrDur_us', 'midpointICI']
medias = df[colunas_interesse].mean()

# Exibir as médias das colunas selecionadas
print("Média das colunas selecionadas:")
print(medias)
