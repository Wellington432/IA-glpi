from services.ia import  perguntar_ia
from services.banco import  salvar_perguntas_respostas


print ("Bem-vindo ao assistente de suporte técnico, sou a Yari! Digite 'sair' para encerrar o programa.")

while True:
    pergunta = input("Digite sua pergunta: ")

    if pergunta.lower() == 'sair':
        print("Encerrando o programa. Até logo!")
        break


    try:

        resposta = perguntar_ia(pergunta)

        print(" Bot:", resposta)

        salvar_perguntas_respostas(pergunta, resposta)

    except Exception as e:
        print("Erro:", e)