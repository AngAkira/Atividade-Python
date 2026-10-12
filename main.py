import pandas as pd
import matplotlib.pyplot as plt

import prep_arquivos as pa
import analise as an
import graficos as gr

#etapa 1
df = pd.read_csv('Atividade2.csv')
dados = pa.preparar_dados(df)

#etapa 2
an.comparar(dados)
#etapa 3

#etapa 4
