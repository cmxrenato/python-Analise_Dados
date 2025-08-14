import pandas as pd
#Se o JSON for aninhado ------------------------
json_data = [
    {
        "id": 1,
        "nome": "Ana",
        "idade": 23,
        "endereco": {"rua": "Rua A", "cidade": "SP"}, #dicionário dentro de dicionário
        "telefones": ["1111-1111", "2222-2222"]
    },
    {
        "id": 2,
        "nome": "Bruno",
        "idade": 25,
        "endereco": {"rua": "Rua B", "cidade": "RJ"},
        "telefones": ["3333-3333"]
    }
]
df = pd.DataFrame(json_data)

# Achatar o JSON usando json_normalize
df = pd.json_normalize(
    json_data,
    sep="_"  # substitui pontos por underline no nome das colunas
)

df.to_excel('planilhas/json_aninhado.xlsx', index=False)