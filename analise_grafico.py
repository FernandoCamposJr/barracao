##Instruções:
##Certifique-se de ter o Matplotlib instalado. Se ainda não tiver, você pode instalá-lo usando o seguinte comando no terminal do PyCharm:
##pip install matplotlib


## gráfico número de clicks por hora do dia:

import pandas as pd
import matplotlib.pyplot as plt

# Caminho completo para o arquivo CSV
file_path = r'C:\Users\ferna\OneDrive\Área de Trabalho\CSV Pycharm\tabela-analise-barracao.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';')

# Verifique o nome da coluna de tempo. Aqui vou assumir que se chama 'Hora'
# Converte a coluna 'Hora' para o formato datetime
df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')

# Extrair a hora do dia
df['Hora_do_dia'] = df['Hora'].dt.hour

# Agrupar o número de cliques por hora do dia
cliques_por_hora = df.groupby('Hora_do_dia')['NofClx'].sum()

# Criar um gráfico de barras para o número de cliques por hora do dia
plt.figure(figsize=(10, 6))
cliques_por_hora.plot(kind='bar', color='lightgreen')

# Adicionar título e rótulos ao gráfico
plt.title('Número de Cliques por Hora do Dia', fontsize=16)
plt.xlabel('Hora do Dia', fontsize=12)
plt.ylabel('Número de Cliques (NofClx)', fontsize=12)

# Exibir o gráfico
plt.xticks(rotation=0)  # Manter os rótulos das horas retos
plt.show()