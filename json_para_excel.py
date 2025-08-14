import pandas as pd

# Exemplo de JSON (poderia vir de uma API ou arquivo)
json_data = [
    {"nome": "Ana", "idade": 23, "cidade": "SP"},
    {"nome": "Bruno", "idade": 25, "cidade": "RJ"},
    {"nome": "Carlos", "idade": 30, "cidade": "BH"}
]

# Converter JSON para DataFrame
df = pd.DataFrame(json_data)

# Salvar em Excel
df.to_excel("planilhas/dados_json_excel.xlsx", index=False)

print("Arquivo Excel criado com sucesso!")


#___________________
#Se o JSON vem de um arquivo
df = pd.read_json("dados.json")
df.to_excel("dados.xlsx", index=False)

#Se o JSON vem de uma API

#import requests
#import pandas as pd

url = "https://api.exemplo.com/dados"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df.to_excel("dados.xlsx", index=False)

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
