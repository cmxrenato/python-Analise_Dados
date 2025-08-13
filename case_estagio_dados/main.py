import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Carregar os dados
df = pd.read_csv('dados_vendas3.csv')

# 2. Checar e tratar valores nulos
#problema que pode deletar linhas inteiras com dados
#print(df.isnull().sum())
#df = df.dropna()

# Mostrar quantidade de nulos apenas na coluna 
print(df['Vendas'].isnull().sum())
print(df['Mes'].isnull().sum())
print(df['Marketing'].isnull().sum())

# Preencher nulos da coluna 'Vendas' com a média
#df['Vendas'] = df['Vendas'].fillna(df['Vendas'].mean())
df['Vendas'] = df['Vendas'].fillna(15000)

df['Marketing'] = df['Marketing'].fillna(15000)

#df.to_csv('dados_vendas3_atualizado.csv', index=False)
#df = pd.read_csv('dados_vendas3_atualizado.csv')



# 3. Estatísticas descritivas
print(df.describe())

# 4. Gráfico de vendas ao longo dos meses
plt.plot(df['Mes'], df['Vendas'], marker='o')
plt.title('Vendas Mensais em 2024')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')
plt.grid(True)
plt.show()

# 5. Modelo de regressão linear
X = df[['Marketing']]  # variável independente / Matriz 2D
y = df['Vendas']       # variável dependente

modelo = LinearRegression()
modelo.fit(X, y)

# 6. Previsão para investimento de R$10.000
investimento = np.array([[10000]]) #Matriz 2D para o predict
previsao = modelo.predict(investimento)
print(f"Previsão de vendas para R$10.000 de marketing: R${previsao[0]:.2f}")

