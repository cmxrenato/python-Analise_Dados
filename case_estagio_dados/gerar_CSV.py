import pandas as pd

# Criar dados do exemplo
dados = {
    "Mes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Vendas": [12000, 13500, None, 14500, 17000, 17500, 18000, 19000, 20000, 21000, 22000, 25000],
    "Marketing": [5000, 6000, 7000, 8000, 8200,5231,9889,1111,8700, 9000, None, 9500]
}

df = pd.DataFrame(dados)

# Salvar como CSV
df.to_csv('dados_vendas3.csv', index=False)

print("Arquivo 'dados_vendas.csv' criado com sucesso!")
