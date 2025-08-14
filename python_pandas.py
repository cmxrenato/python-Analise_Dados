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
print(Fevereiro)

# Total por centro de custo
totais = Fevereiro.groupby('Mês')['Valor'].sum()
print(totais)
#------------------
selecao = df[(df['Ano'] == 2024) & (df['Centro de Custo'] == 'Vendas')]
print(selecao)
total = selecao.groupby('Centro de Custo')['Valor'].sum()
print(total)




#-----------------------
#Selecao = df[(df['Ano'] == 2024) & (df['Centro de Custo'] == 'TI')]
#Selecao = df[(df['Ano'] == 2024)] 


#totais = Selecao.groupby('Centro de Custo')['Valor'].sum().reset_index()



# Calcular percentual de cada centro de custo
#totais = totais.reset_index()
#totais['% do Total'] = (totais['Valor'] / totais['Valor'].sum()) * 100



# Exportar relatório para uma pasta de trabalho nova
#totais.to_excel("relatorio_Fevereiro.xlsx", index=False)
#totais.to_csv("relatorio_2024-2.csv", index=False)

#criando uma nova planilha na mesma pasta de trabalho
#with pd.ExcelWriter("planilhas/despesas_treinamento.xlsx", engine='openpyxl', mode='a') as writer:
#    totais.to_excel(writer, sheet_name='Resumo Janeiro', index=False)



# Filtrar despesas do TI em 2024
#ti_2024 = df[(df['Centro de Custo'] == 'TI') & (df['Ano'] == 2024)]

# Mostrar as 5 primeiras linhas para conferir
#print(ti_2024.head())

# Somar total de despesas do TI em 2024
#total_ti_2024 = ti_2024['Valor'].sum()
#print(f"Total de despesas do TI em 2024: R$ {total_ti_2024:.2f}")

# Exportar para Excel
#ti_2024.to_excel('relatorio_TI_2024.xlsx', index=False)

#print(df.columns)
#print(df)
#print(df.dropna())
#df["Valor"] = df["Valor"].fillna(0)
#df["Categoria"]= df["Categoria"].fillna("Sem valor")
#nova_planilha = df.drop('Categoria',axis=1)
#print(nova_planilha)

#nova_planilha.to_excel('planilhas/despesas_treinamento_nova.xlsx', index=False)