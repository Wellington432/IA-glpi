import sqlite3

conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    perguntas TEXT,
    respostas TEXT
)
''')

conexao.commit()


def salvar_perguntas_respostas(perguntas, respostas):

    cursor.execute('''
    INSERT INTO usuarios (perguntas, respostas)
    VALUES (?, ?)
    ''', (perguntas, respostas))

    conexao.commit()


def carregar_memoria():

    cursor.execute("""
    SELECT perguntas, respostas
    FROM usuarios
    ORDER BY id ASC
    """)

    dados = cursor.fetchall()

    historico = []

    for perguntas, respostas in dados:

        historico.append({
            "role": "user",
            "content": perguntas
        })

        historico.append({
            "role": "assistant",
            "content": respostas
        })

    return historico