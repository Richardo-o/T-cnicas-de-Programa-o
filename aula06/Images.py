from tkinter import filedialog
from PIL import Image, ImageTk

pasta_inicial = ""

def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
filetypes=(("Arquivos de imagem", "*.jpg* . jpeg; *.png"),
           ("Todos os arquivos", "*.*")))
    