RELATÓRIO – ANÁLISE DE DADOS DE SAÚDE (AVC)

Equipe: 

https://github.com/AngAkira

https://github.com/heloisa-flores

1. Objetivo
Analisar o arquivo Atividade2.csv, comparando pacientes com e sem registro de AVC (variável stroke). O programa foi feito em Python, com pandas, Matplotlib e SQLite. Os resultados valem apenas para este conjunto de dados e não indicam, por si só, relação de causa e efeito.

2. Preparação dos dados
O arquivo tem 5.110 registros e 12 características. Só a coluna bmi (IMC) tinha dados ausentes: 201 registros (3,9%). Eles foram preenchidos com a mediana da coluna. O programa mostra 201 ausentes antes do tratamento e 0 depois, o que comprova a limpeza.

3. Análise
Dos 5.110 pacientes, 249 (4,9%) têm registro de AVC e 4.861 não têm.

Comparação entre os grupos (com AVC x sem AVC):
- Idade média: 67,73 x 41,97 anos
- Hipertensão: 26,51% x 8,89%
- Doença cardíaca: 18,88% x 4,71%
- Glicose média: 132,54 x 104,80 mg/dL
- IMC médio: 30,09 x 28,80

A idade é a maior diferença: o grupo com AVC é, em média, 26 anos mais velho. Hipertensão e doença cardíaca são de três a quatro vezes mais frequentes nesse grupo, e a glicose média é maior. O IMC difere pouco. Em proporção, 13,2% dos pacientes com 60 anos ou mais têm registro de AVC, contra 0,4% dos menores de 40.

No tabagismo, ex-fumantes têm a maior taxa de AVC (7,9%), seguidos por fumantes (5,3%) e por quem nunca fumou (4,8%). A categoria "Unknown" (3,0%) significa informação não registrada, não "não fumante", e reúne pacientes mais jovens. Como os ex-fumantes tendem a ser mais velhos, parte da diferença pode ser efeito da idade.

4. Gráficos
- grafico_idade.png: os casos de AVC se concentram nas idades altas (73% têm 60 anos ou mais).
- grafico_hipertensao.png: 26,5% dos pacientes com AVC têm hipertensão, contra 8,9% dos sem AVC.
- Grafico_quantidade.png (análise livre): mostra 249 pacientes com AVC contra 4.861 sem, um forte desequilíbrio que justifica comparar por percentuais e não por contagens.

5. Banco de dados SQLite
Os dados tratados foram gravados na tabela pacientes do arquivo pacientes.db. As consultas retornaram 5.110 registros no total, 249 pacientes com AVC e 498 pacientes com hipertensão, valores iguais aos da análise em pandas.

6. Conclusão
Neste conjunto de dados, os pacientes com registro de AVC são mais velhos e têm mais hipertensão, doença cardíaca e glicose elevada; IMC e tabagismo diferem menos. Essas diferenças são descritivas: as características se relacionam entre si (por exemplo, hipertensão cresce com a idade), o grupo com AVC é pequeno e parte do IMC foi imputada. Não é possível afirmar que alguma delas cause o AVC.

