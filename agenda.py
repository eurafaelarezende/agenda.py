import tkinter as tk

compromissos = []

def salvar_compromisso():
    compromisso = entrada_compromisso.get()
    data = entrada_data.get()

    if compromisso and data:
        compromissos.append(f"{data} - {compromisso}")
        entrada_compromisso.delete(0, tk.END)
        entrada_data.delete(0, tk.END)
        exibir_compromissos()
    else:
        print("Por favor, preencha todos os campos.")

def exibir_compromissos():
    for widget in frame_lista.winfo_children():
        widget.destroy()

    for i, compromisso in enumerate(compromissos):
        compromisso_label = tk.Label(frame_lista, text=compromisso)
        compromisso_label.grid(row=i, column=0, sticky="w")
        
        remover_button = tk.Button(frame_lista, text="Remover", command=lambda i=i: remover_compromisso(i))
        remover_button.grid(row=i, column=1)

def remover_compromisso(index):
    compromissos.pop(index)
    exibir_compromissos()

janela = tk.Tk()
janela.title("Agenda Digital")

rotulo = tk.Label(janela, text="Bem-vindo à sua Agenda Digital!")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui!")
botao.pack()

rotulo_compromisso = tk.Label(janela, text="Digite o compromisso:")
rotulo_compromisso.pack()

entrada_compromisso = tk.Entry(janela, width=30)
entrada_compromisso.pack()

rotulo_data = tk.Label(janela, text="Digite a data (dd/mm/aaaa):")
rotulo_data.pack()

entrada_data = tk.Entry(janela, width=30)
entrada_data.pack()

botao_salvar = tk.Button(janela, text="Salvar Compromisso", command=salvar_compromisso)
botao_salvar.pack()

rotulo_lista = tk.Label(janela, text="Compromissos salvos:", anchor="w", justify="left")
rotulo_lista.pack()

frame_lista = tk.Frame(janela)
frame_lista.pack()

janela.mainloop()
