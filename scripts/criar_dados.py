import pandas as pd
import os

# Gerar dados fictícios
df = pd.DataFrame({
    'categoria': ["grãos", "frutas", "oleaginosas", "animais", "bebida"],
    'países': ['Brasil', 'Bolivia', 'Canadá', 'Dinamarca', 'Estados Unidos'],
    'quantidade Vendas': ['50.000', '20.000', '30.000', '90.000', '40.000'],
    'produto': ['arroz', 'uva', 'feijão', 'vaca', 'leite']
})

# Salvar em Parquet
df.to_parquet('dados/dataset.parquet', engine='pyarrow')

# Salvar em ORC
df.to_orc('dados/dataset.orc')

# Salvar em CSV
df.to_csv("dados/dataset.csv", index=False)

# Salvar em JSON

df.to_json("dados/dataset.json", orient="records", lines=False, force_ascii=False)

print("Arquivos salvos com sucesso!")

# Verificar se a pasta 'dados' existe, se não, cria a pasta
if not os.path.exists('dados'):
    os.makedirs('dados')