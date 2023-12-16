# Importando bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
dados_gasolina = pd.read_csv('gasolina.csv')

# Configurando o estilo do gráfico com o Seaborn
sns.set(style='whitegrid')

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=dados_gasolina, marker='o')

# Adicionando rótulos e título
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvando o gráfico como uma imagem PNG
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()
