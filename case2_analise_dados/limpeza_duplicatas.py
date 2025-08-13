import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#leitura
origem = 'planilhas/controladoria_sem_tratamento_python.xlsx'
destino = 'planilhas/controladoria_com_tratamento_duplicatas.xlsx'
df = pd.read_excel(origem)

#Limpeza de duplicatas
df_limpo = df.drop_duplicates(subset=['fornecedor','numero_documento'])





















#Exportação do arquivo
df_limpo.to_excel(destino, index=False)
