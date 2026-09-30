import tkinter as tk
from tkinter import messagebox
from dados import perguntas

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
        text=f"Você acertou {pontuacao} de {len(perguntas)}!",
        font=("Arial", 16)
    ).pack(pady=20)

    tk.Button(
        janela,
        text="Jogar novamente",
        command=tela_inicial
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Sair",
        command=janela.destroy
    ).pack(pady=10)


tela_inicial()
janela.mainloop()
