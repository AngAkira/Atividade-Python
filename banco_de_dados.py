import sqlite3


def salvar_dados(arquivo):
    conexao = sqlite3.connect('pacientes.db')
    cursor = conexao.cursor()

    # Criação explícita da tabela
    cursor.execute('DROP TABLE IF EXISTS pacientes')
    cursor.execute('''
        CREATE TABLE pacientes (
            id INTEGER PRIMARY KEY,
            gender TEXT,
            age REAL,
            hypertension INTEGER,
            heart_disease INTEGER,
            ever_married TEXT,
            work_type TEXT,
            Residence_type TEXT,
            avg_glucose_level REAL,
            bmi REAL,
            smoking_status TEXT,
            stroke INTEGER
        )
    ''')

    arquivo.to_sql(
        'pacientes',
        conexao,
        if_exists='append',
        index=False
    )
    conexao.commit()

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