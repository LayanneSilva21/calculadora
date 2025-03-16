import tkinter as tk

def mostrar_tela(tela):
    tela_atual.tkraise()  # Coloca a tela atual no topo

# Configuração da janela principal
janela = tk.Tk()
janela.title("App com Múltiplas Telas")
janela.geometry("300x200")

# Contêiner para as telas
container = tk.Frame(janela)
container.pack(fill="both", expand=True)

# Dicionário para armazenar as telas
telas = {}

# Tela principal (Tela 1)
tela1 = tk.Frame(container)
telas["tela1"] = tela1
tela1.grid(row=0, column=0, sticky="nsew")

tk.Label(tela1, text="Tela Principal").pack(pady=20)
tk.Button(tela1, text="Ir para a Tela 2", command=lambda: mostrar_tela(telas["tela2"])).pack()

# Tela 2
tela2 = tk.Frame(container)
telas["tela2"] = tela2
tela2.grid(row=0, column=0, sticky="nsew")

tk.Label(tela2, text="Tela 2").pack(pady=20)
tk.Button(tela2, text="Voltar para a Tela Principal", command=lambda: mostrar_tela(telas["tela1"])).pack()

# Mostrar a primeira tela inicialmente
tela_atual = tela1
mostrar_tela(telas["tela1"])

# Loop principal da aplicação
janela.mainloop()
