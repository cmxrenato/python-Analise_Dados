import pandas as pd

df = pd.read_excel('planilhas/despesas_treinamento.xlsx')

#mostra as 5 primeiras linhas
#print(df.head())

#informações gerais
#print(df.info())

# estatísticas descritivas
#print(df.describe())


# selecionar coluna específica
#print(df['Nome'])


# exportar para Excel
#df.to_excel('saida.xlsx', index=False)

#print(df.tail())

# Filtrar apenas despesas do mês de Fevereiro
# Filtrar apenas despesas do mês de Fevereiro
Fevereiro = df[df['Mês'] == 'Fevereiro']

# Total por centro de custo
totais = Fevereiro.groupby('Categoria')['Valor'].sum()

# Calcular percentual de cada centro de custo
totais = totais.reset_index()
totais['% do Total'] = (totais['Valor'] / totais['Valor'].sum()) * 100

# Exportar relatório para uma pasta de trabalho nova
#totais.to_excel("relatorio_Fevereiro.xlsx", index=False)

#criando uma nova planilha na mesma pasta de trabalho
with pd.ExcelWriter("planilhas/despesas_treinamento.xlsx", engine='openpyxl', mode='a') as writer:
    totais.to_excel(writer, sheet_name='Resumo Janeiro', index=False)

