from groq import Groq
from dotenv import load_dotenv
from banco import salvar_perguntas_respostas, carregar_memoria
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

historico = [
    {
        "role": "system",
        "content": """
        Você é Yari.

        Seu nome sempre é Yari.

        Você deve lembrar informações ditas pelo usuário.
        """
    }
]

# carrega memória antiga
historico += carregar_memoria()

print(" Yari iniciada!")

while True:

    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        break

    historico.append({
        "role": "user",
        "content": pergunta
    })

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=historico
    )

    texto = resposta.choices[0].message.content

    print(" Yari:", texto)

    historico.append({
        "role": "assistant",
        "content": texto
    })

    
    salvar_perguntas_respostas(pergunta, texto)