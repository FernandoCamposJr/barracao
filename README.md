# Análise Acústica de Biologia Usando Python e Pandas

Este repositório contém os scripts e instruções para realizar uma análise acústica de dados de biologia usando **Python**, **Pandas** e **PyCharm**. O objetivo é calcular estatísticas básicas, como média, desvio padrão, valor mínimo e máximo de várias colunas de dados, além de visualizar gráficos.

## Índice

- [Instalação](#instalação)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Importação e Carregamento de Dados CSV](#importação-e-carregamento-de-dados-csv)
- [Análises Realizadas](#análises-realizadas)
  - [Cálculo de Médias](#cálculo-de-médias)  
  - [Cálculo de Desvio Padrão](#cálculo-de-desvio-padrão)
  - [Cálculo de Valor Mínimo](#cálculo-de-valor-mínimo)
  - [Cálculo de Valor Máximo](#cálculo-de-valor-máximo)
  - [Visualização de Gráficos](#visualização-de-gráficos)
- [Contato](#contato)

## Instalação

### 1. Instalar Python

Se ainda não tiver o **Python** instalado, faça o download e a instalação a partir do site oficial:

- [Download Python](https://www.python.org/downloads/)

Durante a instalação, marque a opção "Add Python to PATH".

### 2. Instalar o PyCharm

O **PyCharm** é uma IDE (Ambiente de Desenvolvimento Integrado) recomendada para trabalhar com projetos em Python.

- [Download PyCharm](https://www.jetbrains.com/pycharm/download/)

Instale a versão **Community** (gratuita) para começar.

### 3. Criar um Ambiente Virtual

Após instalar o Python, crie um ambiente virtual para o projeto. No PyCharm, você pode fazer isso criando um novo projeto e selecionando a opção de criar um ambiente virtual (virtual environment).

### 4. Instalar Bibliotecas Necessárias

Dentro do ambiente virtual, use o terminal do PyCharm para instalar as seguintes bibliotecas:

```bash
pip install pandas
pip install matplotlib
```

Importação e Carregamento de Dados CSV
O arquivo CSV é carregado no script usando a biblioteca Pandas. Abaixo está o código para carregar o arquivo CSV:


import pandas as pd

# Caminho completo para o arquivo CSV
file_path = r'C:\Users\ferna\OneDrive\Área de Trabalho\CSV Pycharm\tabela-analise-barracao.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';')

Análises Realizadas
Cálculo de Médias
A média foi calculada para as colunas NofClx, medianKHz, avSPL, TrDur_us e midpointICI:

colunas_interesse = ['NofClx', 'medianKHz', 'avSPL', 'TrDur_us', 'midpointICI']
medias = df[colunas_interesse].mean()
print(medias)

Cálculo de Desvio Padrão
Para calcular o desvio padrão das mesmas colunas, usamos o seguinte código:

desvios = df[colunas_interesse].std()
print(desvios)

Cálculo de Valor Mínimo
O valor mínimo de cada coluna foi calculado com:

minimos = df[colunas_interesse].min()
print(minimos)

Cálculo de Valor Máximo
O valor máximo de cada coluna foi calculado com:

maximos = df[colunas_interesse].max()
print(maximos)

Visualização de Gráficos
Um gráfico de barras foi gerado para visualizar o número de cliques (NofClx) por hora do dia:

df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')
df['Hora_do_dia'] = df['Hora'].dt.hour
cliques_por_hora = df.groupby('Hora_do_dia')['NofClx'].sum()

cliques_por_hora.plot(kind='bar', color='lightgreen')
plt.title('Número de Cliques por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Número de Cliques (NofClx)')
plt.xticks(rotation=0)
plt.show()

Legenda das Colunas
Line: número de linhas e de cadeias de cliques de golfinhos
File: nome do arquivo de áacústico analisado
Data: data de detecção das cadeias de cliques
Hora: hora de detecção das cadeias de cliques
NofClx: número de cliques por cadeia
medianKHz: frequência mediana dos cliques em cada cadeia
avSPL: média do nível de pressão sonora (sound pressure level, no inglês) dos cliques de cada cadeia
TrDur_us: duração das cadeias de cliques
midpointICI: intervalo entre cliques médio das cadeias


Contato
Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato.

Nome: Fernando César Almeida de Campos Júnior
E-mail: fcacamposjr@gmail.com





