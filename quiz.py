import tkinter as tk
from tkinter import messagebox

# Perguntas e respostas
perguntas = [
    {"pergunta": "Qual é a capital do Brasil?", "opcoes": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"], "resposta": "Brasília"},
    {"pergunta": "Qual é o maior planeta do Sistema Solar?", "opcoes": ["Terra", "Marte", "Júpiter", "Saturno"], "resposta": "Júpiter"},
    {"pergunta": "Quantos continentes existem no mundo?", "opcoes": ["5", "6", "7", "8"], "resposta": "7"}
]

# Variáveis globais
indice_pergunta = 0
pontuacao = 0

def verificar_resposta():
    global indice_pergunta, pontuacao
    resposta_selecionada = resposta_var.get()
    if resposta_selecionada == perguntas[indice_pergunta]["resposta"]:
        pontuacao += 1
    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        carregar_pergunta()
    else:
        finalizar_quiz()

def carregar_pergunta():
    pergunta_label.config(text=perguntas[indice_pergunta]["pergunta"])
    for i, opcao in enumerate(perguntas[indice_pergunta]["opcoes"]):
        botoes_opcoes[i].config(text=opcao, value=opcao)

def finalizar_quiz():
    messagebox.showinfo("Quiz Finalizado", f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
    janela.quit()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Quiz")
janela.geometry("400x300")

pergunta_label = tk.Label(janela, text="", font=("Arial", 14), wraplength=380, justify="center")
pergunta_label.pack(pady=20)

resposta_var = tk.StringVar()
botoes_opcoes = []
for i in range(4):
    botao = tk.Radiobutton(janela, text="", variable=resposta_var, value="", font=("Arial", 12))
    botao.pack(anchor="w", padx=20)
    botoes_opcoes.append(botao)

botao_confirmar = tk.Button(janela, text="Confirmar", command=verificar_resposta)
botao_confirmar.pack(pady=20)

carregar_pergunta()

janela.mainloop()
