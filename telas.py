import tkinter as tk
from tkinter import messagebox

def autenticar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Tela de Login")

# Widgets para login
tk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=20, pady=20)
entrada_usuario = tk.Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=20, pady=20)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=10)

botao_login = tk.Button(janela, text="Login", command=autenticar)
botao_login.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar o loop principal
janela.mainloop()

        