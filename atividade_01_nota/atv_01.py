# Importando tkinter

from tkinter import *

# Armazenando o Tk inter dentro de uma váriavel chamada tela

tela = Tk()

# Definindo o tamanho da tela

tela.geometry("700x600")


# Ajusatando as configurações da tela, nesse caso a cor de fundo da tela.

tela.configure(background='#242424')

# Criando as labels que informa o que o usuário está digitando         # O comando .place é para deslocar as labels
# Primeiro é criado uma variável que recebe o valor de uma Label informamos que ela vai aparecer na tela, o texto que ela vai mostrar e depois é definido as cores sendo bg o background e o fg foreground 

lbl_nome = Label(tela, text = "Nome: ", bg="#242424", fg="#ffffff").place (x=220, y=0)
lbl_idade = Label(tela, text= "Idade: ", bg="#242424", fg="#ffffff").place(x=220, y=30)
lbl_tel = Label(tela, text="Telefone: ", bg="#242424", fg="#ffffff").place(x=200, y=58)
lbl_parentesco = Label(tela, text="Grau de parentesco: ", bg="#242424", fg="#ffffff").place(x=160, y=85)


# Criando os espaços para digitar. O .pack() serve para deixar um em baixo do outro
txt_nome = Entry(tela, width=20, borderwidth=5 )
txt_nome.pack()


txt_idade = Entry(tela, width=20, borderwidth=5)
txt_idade.pack()


txt_telefone= Entry(tela, width=20, borderwidth=5 )
txt_telefone.pack()


txt_parentesco = Entry(tela, width=20, borderwidth=5 )
txt_parentesco.pack()


#Aqui é criado a função do botão 

def meu_click():

    # Tive que criar uma variável idade pegar o valor de txt_idade e converter ele para inteiro.

    idade = int(txt_idade.get())

    # Mostrando a estrutura condicional que funcina da seguinte forma. Pegamos a variável idade criada anteriormente e é feito um if caso a idade seja >= 18 deve aparecer a mensagem_voto = "Pode Votar" caso contrario a mensagem de voto deve mostrar "Não pode Votar!"
    if idade >= 18:
        mensagem_voto = "Pode Votar!"
    else: mensagem_voto = "Não Pode Votar!"
    
    # aqui cria o a label que vai mostrar o parente cadastrado onde que por meio do parâmetro get conseguimos pegar e após isso concatenar com outras variáveis buscadas do "formulário"

    txt_parente= Label(tela, text="" + "Nome: " + txt_nome.get() + " | " + "Idade: " + txt_idade.get() + " | " + "Telefone: " + txt_telefone.get() + " | " + "Grau parentesco: " + txt_parentesco.get() + " | " +  mensagem_voto)
    
    txt_parente.pack()
    
    

   
   # Aqui é feito o botão de cadastrar que é do tipo button e o texto presente dentro dele é Cadastra, passamos o comando para ele no caso meu_click q executa toda aquela função e nesse botão foi colocado um padding de 20px como mostrado no btn_botao.pack(pady=20)
    
btn_botao = Button(tela, text="Cadastrar", command=meu_click, bg="#1F6AA0", fg="#ffffff")
btn_botao.pack(pady=20)

lbl_p1 = Label(tela, text= "Nome: Zileide Mariano| Idade: 54 | Telefone: (13)99673-1592 | Grau parentesco: 3º | Pode Votar!")
lbl_p1.pack()

lbl_p2 = Label(tela, text= "Nome: Jailson Mariano | Idade: 55 | Telefone: (13)99623-3456 | Grau parentesco: 3º | Pode Votar!")
lbl_p2.pack()

lbl_p3 = Label(tela, text= "Nome: José Mariano | Idade: 54 | Telefone: (13)99640-3654 | Grau parentesco: 3º | Pode Votar!")
lbl_p3.pack()

lbl_p4 = Label(tela, text= "Nome: Maria Julia | Idade: 87 | Telefone: (13)99343-3633 | Grau parentesco: 2º | Pode Votar!")
lbl_p4.pack()


 # tela main loop para permitir que a aplicação permaneça aberta

tela.mainloop()
