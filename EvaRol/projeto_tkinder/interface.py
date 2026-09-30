import tkinter as tk
from tkinter import messagebox




perguntas = [
    {
        "pergunta": "O que significa DNA?",
        "opcoes": [
            "Ácido desoxirribonucleico",
            "Ácido ribonucleico",
            "Ácido nucleico duplo",
            "Desoxirribose nucleica ativa"
        ],
        "resposta": "Ácido desoxirribonucleico"
    },
    {
        "pergunta": "Qual civilização é associada ao surgimento da democracia em Atenas?",
        "opcoes": [
            "Romana",
            "Egípcia",
            "Grega",
            "Persa"
        ],
        "resposta": "Grega"
    },
    {
        "pergunta": "Quanto é 15 x 15 - 10 x 10?",
        "opcoes": [
            "75",
            "100",
            "125",
            "150"
        ],
        "resposta": "125"
    },
    {
        "pergunta": "Qual é o maior oceano da Terra?",
        "opcoes": [
            "Atlântico",
            "Índico",
            "Ártico",
            "Pacífico"
        ],
        "resposta": "Pacífico"
    },
    {
        "pergunta": "Qual é a unidade de força no Sistema Internacional?",
        "opcoes": [
            "Joule",
            "Newton",
            "Pascal",
            "Watt"
        ],
        "resposta": "Newton"
    },
    {
        "pergunta": "Qual é o nome do processo de transformação do estado líquido para o gasoso?",
        "opcoes": [
            "Condensação",
            "Solidificação",
            "Fusão",
            "Vaporização"
        ],
        "resposta": "Vaporização"
    },
    {
        "pergunta": "Qual filósofo é associado à frase 'Penso, logo existo'?",
        "opcoes": [
            "Kant",
            "Descartes",
            "Nietzsche",
            "Rousseau"
        ],
        "resposta": "Descartes"
    }
]



indice = 0
pontuacao = 0




janela = tk.Tk()
janela.title("Quiz Master")
janela.geometry("600x400")
janela.resizable(False, False)




def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()




def tela_inicial():
    limpar_tela()

    tk.Label(
        janela,
        text="QUIZ MASTER",
        font=("Arial", 28, "bold")
    ).pack(pady=60)

    tk.Label(
        janela,
        text="Teste seus conhecimentos!",
        font=("Arial", 14)
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Iniciar Quiz",
        font=("Arial", 14),
        command=iniciar_quiz
    ).pack(pady=30)




def iniciar_quiz():
    global indice, pontuacao

    indice = 0
    pontuacao = 0

    mostrar_pergunta()




def mostrar_pergunta():
    limpar_tela()

    pergunta_atual = perguntas[indice]

    tk.Label(
        janela,
        text=f"Pergunta {indice + 1} de {len(perguntas)}",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Label(
        janela,
        text=pergunta_atual["pergunta"],
        font=("Arial", 16),
        wraplength=500
    ).pack(pady=20)

    resposta = tk.StringVar()

    for opcao in pergunta_atual["opcoes"]:
        tk.Radiobutton(
            janela,
            text=opcao,
            variable=resposta,
            value=opcao,
            font=("Arial", 12)
        ).pack(anchor="w", padx=150)

    tk.Button(
        janela,
        text="Próxima",
        font=("Arial", 12),
        command=lambda: verificar_resposta(resposta)
    ).pack(pady=25)




def verificar_resposta(resposta):
    global indice, pontuacao

    if not resposta.get():
        messagebox.showwarning(
            "Atenção",
            "Selecione uma resposta."
        )
        return

    if resposta.get() == perguntas[indice]["resposta"]:
        pontuacao += 1

    indice += 1

    if indice < len(perguntas):
        mostrar_pergunta()
    else:
        tela_resultado()



def tela_resultado():
    limpar_tela()

    tk.Label(
        janela,
        text="Resultado",
        font=("Arial", 28, "bold")
    ).pack(pady=60)

    tk.Label(
        janela,
        text=f"Você acertou {pontuacao} de {len(perguntas)} perguntas!",
        font=("Arial", 16)
    ).pack(pady=20)

    tk.Button(
        janela,
        text="Jogar novamente",
        font=("Arial", 13),
        command=tela_inicial
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Sair",
        font=("Arial", 13),
        command=janela.destroy
    ).pack(pady=10)




tela_inicial()

janela.mainloop()
