def comparar(arquivo):
    com_avc = arquivo['stroke'] == 1
    sem_avc = arquivo['stroke'] == 0
    print(f"\nComparando dados, com avc:{com_avc.sum()}")
    print(f"Idade: {arquivo.loc[com_avc, 'age'].mean()}")
    print(f"Hipertensão: {arquivo.loc[com_avc, 'hypertension'].sum()}")
    print(f"Doença cardíaca: {arquivo.loc[com_avc, 'heart_disease'].sum()}")
    print(f"Nivel médio de glicose: {arquivo.loc[com_avc, 'glucose_level'].sum()}")

    print(f"\nComparando dados, sem avc:{sem_avc.sum()}")
    print(f"Idade: {arquivo.loc[sem_avc, 'age'].mean()}")
    print(f"Hipertensão: {arquivo.loc[sem_avc, 'hypertension'].sum()}")
    print(f"Doença cardíaca: {arquivo.loc[sem_avc, 'heart_disease'].sum()}")
    print(f"Nivel medio de glicose: {arquivo.loc[sem_avc, 'glucose_level'].sum()}")

#•	idade;
#hipertensão;
#doença cardíaca;
#nível médio de glicose;
#IMC;
#situação de tabagismo.
#