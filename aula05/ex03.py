from tkinter import *

tela = Tk()

#Título na barra de tarefas
tela.title("Fatec Registro")

tela.geometry("700x600")
tela.resizable(True, True)
tela.maxsize(width=800, height=700)
tela.minsize(width=500, height=300)

lbl_nome = Label(tela, text="Nome", font="Arial 20 bold italic"),


tela.mainloop()