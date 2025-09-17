from tkinter import *

tela = Tk()

tela.geometry("700x600")

lbl_nome = Label(tela, text = "Nome: ").place (x=220, y=0)
lbl_idade = Label(tela, text= "Idade: ").place(x=220, y=30)
lbl_tel = Label(tela, text="Telefone: ").place(x=200, y=58)
lbl_parentesco = Label(tela, text="Grau de parentesco: ").place(x=160, y=85)

txt_nome = Entry(tela, width=20, borderwidth=5, bg="white")
txt_nome.pack()
txt_nome.insert(0, "")

txt_idade = Entry(tela, width=20, borderwidth=5, bg="white")
txt_idade.pack()
txt_idade.insert(0, "")

txt_telefone= Entry(tela, width=20, borderwidth=5, bg="white")
txt_telefone.pack()
txt_telefone.insert(0, "")

txt_parentesco = Entry(tela, width=20, borderwidth=5, bg='white' )
txt_parentesco.pack()
txt_parentesco.insert(0, "")


def meu_click():
    botao= Label(tela, text="" + "Nome: " + txt_nome.get() + "\n" + "Idade: " + txt_idade.get() + "\n" + "Telefone: " + txt_telefone.get() + "\n" + "Grau parentesco: " + txt_parentesco.get())
    botao.pack()
    
    
btn_botao = Button(tela, text="Salvar", command=meu_click)
btn_botao.pack()



tela.mainloop()
