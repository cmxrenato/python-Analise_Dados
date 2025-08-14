import pandas as pd

# === CONFIGURAÇÕES ===
arquivo_entrada = "planilhas/planilha_com_duplicatas.xlsx"  
arquivo_saida = "planilhas/planilha_sem_duplicatas3.xlsx"    

# Ler a planilha
df = pd.read_excel(arquivo_entrada)

# Perguntar ao usuário
print("Opções para remover duplicatas:")
print("1 - Manter a primeira ocorrência")
print("2 - Manter a última ocorrência")
print("3 - Remover todas as ocorrências duplicadas")

opcao = input("Escolha (1, 2 ou 3): ")

if opcao == "1":
    df_limpo = df.drop_duplicates(keep="first")
elif opcao == "2":
    df_limpo = df.drop_duplicates(keep="last")
elif opcao == "3":
    df_limpo = df.drop_duplicates(keep=False)
else:
    print("Opção inválida.")
    exit()

# Salvar planilha limpa
df_limpo.to_excel(arquivo_saida, index=False)

print(f"Planilha limpa salva como: {arquivo_saida}")
