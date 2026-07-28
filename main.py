import pandas as pd

dados = {
    'Produto': ['X-Tudo', 'X-Salada', 'Refrigerante', 'X-Tudo', 'Refrigerante', 'X-Salada'],
    'Categoria': ['Lanche', 'Lanche', 'Bebida', 'Lanche', 'Bebida', 'Lanche'],
    'Quantidade': [2, 1, 3, 1, 2, 2],
    'Preco_Unitario': [25.0, 20.0, 6.0, 25.0, 6.0, 20.0]
}

df = pd.DataFrame(dados)
print("--- Tabela Original ---")
print(df)