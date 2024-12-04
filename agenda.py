import tkinter as tk
janela = tk.Tk() 
janela.title("Agenda Digital")
rotulo = tk.Label(janela, text="Bem-vindo à sua Agenda Digital!") 
rotulo.pack()
botao = tk.Button(janela, text="Clique aqui!")
botao.pack()  
janela.mainloop()  
