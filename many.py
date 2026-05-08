import sqlite3

# CONEXÃO COM O BANCO
conexao = sqlite3.connect("dados.db")

cursor = conexao.cursor()

# TABELA DE USUÁRIOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarioos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT,
    IDADE INTEGER
)
""")

# TABELA DE MENSAGENS
cursor.execute("""
CREATE TABLE IF NOT EXISTS mensagens (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    mensagem TEXT
)
""")

conexao.commit()










def mostrar_tempo():

    print("O tempo hoje está ensolarado!")


def mostrar_noticias():

    print("As notícias de hoje são: ...")


def mostrar_piada():

    print("Por que o computador foi ao médico?")
    print("Porque ele estava com um vírus!")


def mostrar_historico(nome_usuario):

    cursor.execute(
        "SELECT mensagem FROM mensagens WHERE usuario = ?",
        (nome_usuario,)
    )

    mensagens = cursor.fetchall()

    print("\nHistórico de mensagens:")

    for msg in mensagens:
        print("-", msg[0])


def salvar_mensagem(usuario, mensagem):

    cursor.execute(
        "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
        (usuario, mensagem)
    )

    conexao.commit()



nome = input("Digite seu nome: ")

cursor.execute(
    "SELECT nome FROM usuarioos WHERE nome = ?",
    (nome,)
)

pessoasexist = cursor.fetchone()

if pessoasexist:

    print("Usuário encontrado no banco de dados.")
    print(f"Bem-vindo de volta, {pessoasexist[0]}!")

else:

    cursor.execute(
        "INSERT INTO usuarioos (NOME) VALUES (?)",
        (nome,)
    )

    conexao.commit()

    print("Seja bem-vindo!")




while True:

    message = input(
        "\nDigite uma mensagem (ou 'sair' para encerrar): "
    ).lower()

    
    salvar_mensagem(nome, message)

    if message in ["sair", "tchau", "adeus", "até mais", "xau"]:

        print("Encerrando o programa. Até mais!")
        break

    print("\nOi! Como posso ajudar você hoje?")

     
    if any(message in opt for opt in ["1", "tempo", "clima"]):

        mostrar_tempo()
    if any(message in opt for opt in ["2", "notícias", "news"]):

        mostrar_noticias()   
    if any(message in opt for opt in ["3", "piadas", "jokes"]):

        mostrar_piada()
    if any(message in opt for opt in ["4", "histórico", "historico", "history"]):

        mostrar_historico(nome)


# FECHAR BANCO
conexao.close()