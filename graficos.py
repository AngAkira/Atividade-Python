import matplotlib.pyplot as plt

def grafico_idade(arquivo):
    idades = arquivo.loc[arquivo['stroke'] == 1, 'age']

    idades.plot(kind='hist', bins=10, edgecolor='black')

    plt.title('Distribuição das idades dos pacientes com AVC')
    plt.xlabel('Idade (anos)')
    plt.ylabel('Quantidade de pacientes')
    plt.tight_layout()
    plt.savefig('grafico_idade.png', dpi=150)
    plt.show()

def grafico_hipertensao(arquivo):
    com_avc = arquivo.loc[arquivo['stroke'] == 1, 'hypertension'].mean() * 100
    sem_avc = arquivo.loc[arquivo['stroke'] == 0, 'hypertension'].mean() * 100

    plt.bar(['Com AVC', 'Sem AVC'], [com_avc, sem_avc])

    plt.title('Comparação de hipertensão entre pacientes')
    plt.xlabel('Grupo de pacientes')
    plt.ylabel('Pacientes com hipertensão (%)')
    plt.tight_layout()
    plt.savefig('grafico_hipertensao.png', dpi=150)
    plt.show()

def grafico_quantidade(arquivo):
    quantidades = arquivo['stroke'].value_counts()

    plt.bar(
        ['Sem AVC', 'Com AVC'],
        [quantidades.get(0, 0), quantidades.get(1, 0)]
    )

    plt.title('Quantidade de pacientes por registro de AVC')
    plt.xlabel('Registro de AVC')
    plt.ylabel('Quantidade de pacientes')
    plt.tight_layout()
    plt.savefig('Grafico_quantidade.png', dpi=150)
    plt.show()
    print("\n\nO gráfico foi escolhido para visualizar a quantidade de pacientes com e sem registro de AVC no conjunto de dados."
          " Essa informação permite identificar a diferença no tamanho dos grupos e perceber se existe um desequilíbrio na distribuição dos registros."
          " Isso é relevante para interpretar os outros gráficos, pois os grupos possuem quantidades diferentes de pacientes.")