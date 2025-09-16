from tkinter import *
from tkinter.ttk import *


tela = Tk()
tela.title("Radio Buttons")

# Cor da tela
tela.configure(background='#1e3743')

# Configurar tamanho da tela
tela.geometry("700x600")

# Variável para os RadioButtons
sexo_var = StringVar()
sexo_var.set("m")  # Valor padrão

# Variável para o Checkbutton
check_var = StringVar(value="Off")

# Label para título
lbl_titulo = Label(tela, text="Selecione seu sexo:", background="#1e3743", foreground="white")
lbl_titulo.place(x=20, y=10)

# Botões de opção (RadioButtons)
rdb_buttonm = Radiobutton(tela, text="M", variable=sexo_var, value="m")
rdb_buttonm.place(x=20, y=40)

rdb_buttonf = Radiobutton(tela, text="F", variable=sexo_var, value="f")
rdb_buttonf.place(x=20, y=70)

# Checkbutton
chk_button = Checkbutton(tela, text="Check box", variable=check_var, onvalue="On", offvalue="Off")
chk_button.place(x=20, y=110)
chk_button.state(['!selected'])  # Deselecionar inicialmente

# Combobox
lbl_cidade = Label(tela, text="Selecione sua cidade:", background="#1e3743", foreground="white")
lbl_cidade.place(x=20, y=160)

combo = Combobox(tela, state="readonly")
combo['values'] = ("Iguape", "Ilha Comprida", "Registro", "Jacupiranga", "Cajati")
combo.current(1)  # Define o item selecionado
combo.place(x=20, y=190)

tela.mainloop()
