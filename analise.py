def comparar(arquivo):
    com_avc = arquivo['stroke'] == 1
    sem_avc = arquivo['stroke'] == 0

    # Idade
    print(
        f"Idade média: com AVC = {arquivo.loc[com_avc, 'age'].mean():.2f} | "
        f"sem AVC = {arquivo.loc[sem_avc, 'age'].mean():.2f}"
    )

    # Hipertensão
    print(
        f"Hipertensão: com AVC = {arquivo.loc[com_avc, 'hypertension'].mean() * 100:.2f}% | "
        f"sem AVC = {arquivo.loc[sem_avc, 'hypertension'].mean() * 100:.2f}%"
    )

    # Doença cardíaca
    print(
        f"Doença cardíaca: com AVC = {arquivo.loc[com_avc, 'heart_disease'].mean() * 100:.2f}% | "
        f"sem AVC = {arquivo.loc[sem_avc, 'heart_disease'].mean() * 100:.2f}%"
    )

    # Glicose
    print(
        f"Glicose média: com AVC = {arquivo.loc[com_avc, 'avg_glucose_level'].mean():.2f} | "
        f"sem AVC = {arquivo.loc[sem_avc, 'avg_glucose_level'].mean():.2f}"
    )

    # IMC
    print(
        f"IMC médio: com AVC = {arquivo.loc[com_avc, 'bmi'].mean():.2f} | "
        f"sem AVC = {arquivo.loc[sem_avc, 'bmi'].mean():.2f}"
    )
    #Situação de tabagismo
    print("\nTabagismo com AVC:")
    print(arquivo.loc[com_avc, 'smoking_status'].value_counts())

    print("\nTabagismo sem AVC:")
    print(arquivo.loc[sem_avc, 'smoking_status'].value_counts())
    agrupamentos(arquivo)



def interpretacao():
        print("\n--- Interpretação dos resultados ---")
        print(
            "Em proporção, ex-fumantes têm a maior taxa de AVC. A categoria "
            "'Unknown' (não informado) tem a menor, mas não significa 'não fumante': "
            "ela concentra pacientes mais jovens, incluindo muitas crianças."
        )

        print(
            "Essas diferenças descrevem os dados analisados e não comprovam "
            "relações de causa e efeito."
        )
        print(

            "Os pacientes com registro de AVC apresentaram maior idade média "
            "e maiores proporções de hipertensão e doença cardíaca. "
            "A média de glicose também foi superior nesse grupo, enquanto "
            "a diferença no IMC foi menor."
        )

        print(
            "A distribuição do tabagismo pode ser observada pelas quantidades "
            "de pacientes em cada categoria."
        )

        print(
            "Essas diferenças descrevem os dados analisados e não comprovam "
            "relações de causa e efeito."
        )

def agrupamentos(arquivo):
    arquivo = arquivo.copy()
    arquivo['grupo'] = arquivo['stroke'].map({0: 'Sem AVC', 1: 'Com AVC'})

    print("\n--- Agrupamento: média, mediana e desvio padrão por grupo ---")
    print(arquivo.groupby('grupo')[['age', 'avg_glucose_level', 'bmi']]
          .agg(['mean', 'median', 'std']).round(2).T)

    print("\n--- Percentual de pacientes com AVC em cada subgrupo ---")
    for nome, filtro in [
        ("60 anos ou mais", arquivo['age'] >= 60),
        ("Menos de 40 anos", arquivo['age'] < 40),
        ("Hipertensos", arquivo['hypertension'] == 1),
        ("Não hipertensos", arquivo['hypertension'] == 0),
        ("Com doença cardíaca", arquivo['heart_disease'] == 1),
        ("Sem doença cardíaca", arquivo['heart_disease'] == 0),
        ("Glicose acima de 125", arquivo['avg_glucose_level'] > 125),
    ]:
        print(f"{nome}: {filtro.sum()} pacientes | "
              f"{arquivo.loc[filtro, 'stroke'].mean() * 100:.2f}% com AVC")

    print("\n--- Percentual de AVC por situação de tabagismo ---")
    print((arquivo.groupby('smoking_status')['stroke'].mean() * 100)
          .round(2).sort_values(ascending=False))

