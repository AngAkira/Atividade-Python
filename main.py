import pandas as pd

import prep_arquivos as pa
import analise as an
import graficos as gr
import banco_de_dados as ba
#etapa 1
df = pd.read_csv('Atividade2.csv')
dados = pa.preparar_dados(df)

#etapa 2
an.comparar(dados)
an.interpretacao()

#etapa 3
gr.grafico_idade(dados)
gr.grafico_hipertensao(dados)
gr.grafico_quantidade(dados)

#etapa 4
ba.salvar_dados(dados)
