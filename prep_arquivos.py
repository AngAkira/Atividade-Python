
def preparar_dados(arquivo):
    qtd_registros = len(arquivo)
    dimensoes = arquivo.shape
    caracteristicas = arquivo.columns.tolist()
    dados_ausentes = arquivo.isnull().sum()
    total_dados_ausentes = arquivo.isnull().sum().sum()

    print(f"Quantidade de registros: {qtd_registros}")
    print(f"Quantidade de linhas e colunas: {dimensoes}")
    print(f"Características disponíveis: {caracteristicas}")
    print(f"\nDados ausentes por característica: {dados_ausentes}")
    print(f"\nTotal dados ausentes: {total_dados_ausentes}")

    if total_dados_ausentes > 0:
        print("Existem dados ausentes. Iniciando tratamento...")
        for coluna in arquivo.columns:
            if arquivo[coluna].isnull().sum() > 0:
                if arquivo[coluna].dtype == "object":
                    arquivo[coluna] = arquivo[coluna].fillna(
                        arquivo[coluna].mode()[0]
                    )
                else:
                    arquivo[coluna] = arquivo[coluna].fillna(
                        arquivo[coluna].median()
                    )
    else:
        print("Não existem dados ausentes.")

    print("\nDados ausentes após o tratamento:")
    print(arquivo.isnull().sum())
    print("\nTotal após o tratamento:",
          arquivo.isnull().sum().sum())
    print()
    return arquivo
