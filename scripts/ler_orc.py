import pandas as pd
import pyarrow as pa
import pyarrow.orc as orc
import os

# Criando o DataFrame
df = pd.DataFrame({
    'categoria': ["grãos", "frutas", "oleaginosas", "animais", "bebida"],
    'países': ['Brasil', 'Bolivia', 'Canadá', 'Dinamarca', 'Estados Unidos'],
    'quantidade Vendas': ['50.000', '20.000', '30.000', '90.000', '40.000'],
    'produto': ['arroz', 'uva', 'feijão', 'vaca', 'leite']
})


# Garantir que o diretório de destino exista
orc_dir = 'dados'
if not os.path.exists(orc_dir):
    os.makedirs(orc_dir)

# Convertendo o DataFrame para Table do PyArrow
table = pa.Table.from_pandas(df)

# Caminho do arquivo ORC
orc_file = os.path.join(orc_dir, 'vendas_produtos.orc')

# Salvando a tabela como arquivo ORC
with open(orc_file, 'wb') as f:
    orc.write_table(table, f)

print(f"Arquivo ORC salvo em: {orc_file}")
