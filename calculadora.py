import tkinter as tk

def clique(botao):
    atual = entrada.get()
    if botao == 'C':
        entrada.delete(0, tk.END)
    elif botao == '=':
        try:
            resultado = eval(atual)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, 'Erro')
    else:
        entrada.insert(tk.END, botao)

janela = tk.Tk()
janela.title('Calculadora')

entrada = tk.Entry(janela, width=20, font=('lucida', 18), justify='right')
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

linha = 1
coluna = 0

for botao in botoes:
    cmd = lambda b=botao: clique(b)
    tk.Button(janela, text=botao, width=5, height=2, command=cmd).grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

janela.mainloop()
