import tkinter as tk

janela = tk.Tk()

var_aviao = tk.StringVar()

botao_classeeconomica = tk.Radiobutton(text = "Classe Econômica", variable = var_aviao, value = "Classe Econômica")
botao_classeexecutiva = tk.Radiobutton(text = "Classe Executiva", variable = var_aviao, value = "Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text = "Primeira Classe", variable = var_aviao, value = "Primeira Classe")
botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)

def enviar():
    print(var_aviao.get())

botao_enviar = tk.Button(text = "Enviar", command = enviar)
botao_enviar.grid(row = 1, column = 0)

tk.mainloop()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text = "Deseja receber e-mail promocionais?", variable = var_promocoes)
checkbox_promocoes.grid(row = 0, column = 0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text = "Aceitar termos de Uso e Políticas de Privacidade", variable = var_promocoes)
checkbox_politicas.grid(row = 1, column = 0)

def enviar():
    if var_promocoes.get():
        print('Usuário deseja receber promoções')
    else:
        print('Usuário NÃO deseja receber promoções')
    if var_politicas.get():
        print('Usuário concordou com Termos de Uso e Políticas de Privacidade')
    else:
        print('Usuário NÃO concordou')

botao_enviar = tk.Button (text="Enviar", command = enviar)
botao_enviar.grid(row = 2, column = 0)

janela.mainloop()