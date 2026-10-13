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


def interpretacao():
        print("\n--- Interpretação dos resultados ---")

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



