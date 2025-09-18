from tkinter import *

tela = Tk()

tela.geometry("700x600")

tela.configure(background='#1e3743')

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
    botao= Label(tela, text="" + "Nome: " + txt_nome.get() + " | " + "Idade: " + txt_idade.get() + " | " + "Telefone: " + txt_telefone.get() + " | " + "Grau parentesco: " + txt_parentesco.get())
    botao.pack()
    
    

   
    
btn_botao = Button(tela, text="Cadastrar", command=meu_click)
btn_botao.pack()

lbl_p1 = Label(tela, text= "Nome: Zileide Mariano| Idade: 54 | Telefone: (13)99673-1592 | Grau parentesco: 3º")
lbl_p1.pack()

lbl_p2 = Label(tela, text= "Nome: Jailson Mariano | Idade: 55 | Telefone: (13)99623-3456 | Grau parentesco: 3º")
lbl_p2.pack()

lbl_p3 = Label(tela, text= "Nome: José Mariano | Idade: 54 | Telefone: (13)99640-3654 | Grau parentesco: 3º")
lbl_p3.pack()

lbl_p4 = Label(tela, text= "Nome: Maria Julia | Idade: 87 | Telefone: (13)99343-3633 | Grau parentesco: 2º")
lbl_p4.pack()

tela.mainloop()
