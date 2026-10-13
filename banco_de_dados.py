
import sqlite3


def salvar_dados(arquivo):
    conexao = sqlite3.connect('pacientes.db')

    arquivo.to_sql(
        'pacientes',
        conexao,
        if_exists='replace',
        index=False
    )

    cursor = conexao.cursor()

    # Consulta 1: quantidade total de registros
    cursor.execute('SELECT COUNT(*) FROM pacientes')
    print("Total de registros:", cursor.fetchone()[0])

    # Consulta 2: pacientes com AVC
    cursor.execute('SELECT COUNT(*) FROM pacientes WHERE stroke = 1')
    print("Pacientes com AVC:", cursor.fetchone()[0])

    # Consulta 3: pacientes com hipertensão
    cursor.execute('SELECT COUNT(*) FROM pacientes WHERE hypertension = 1')
    print("Pacientes com hipertensão:", cursor.fetchone()[0])

    conexao.close()
