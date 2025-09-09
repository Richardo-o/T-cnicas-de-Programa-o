from tkinter import *

tela = Tk()

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o nome: ")

txt_email = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_email.pack()
txt_email.insert(0, "Digite o e-mail: ")

txt_telefone = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_telefone.pack()
txt_telefone.insert(0, "Digite o telefone: ")

txt_endereco = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_endereco.pack()
txt_endereco.insert(0, "Digite o endereço: ")

def meu_click():
    lbl_hello= Label(tela, text="Bem Vindo " + txt_nome.get())
    lbl_hello.pack()

btn_botao = Button(tela, text="Cadastrar Cliente", command=meu_click)
btn_botao.pack()

tela.mainloop()