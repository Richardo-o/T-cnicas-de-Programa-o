from tkinter import *

tela = Tk()

#Título na barra de tarefas
tela.title("Fatec Registro")
#Configuração da cor tela (opcional)
tela.configure(background='#1e3743')
#Configuração do tamanho da tela
tela.geometry("700x600")

tela.resizable(True, True)
#Tamanho maximo que a tela pode chegar
tela.maxsize(width=800, height=700)
#Tamanho minimo que a tela pode chegar
tela.minsize(width=500, height=300)

lbl_teste = Label(tela, text = "TESTE").place (x=10, y=10)
lbl_cpf = Label(tela, text= "CPF").place(x=10, y=50)


tela.mainloop()