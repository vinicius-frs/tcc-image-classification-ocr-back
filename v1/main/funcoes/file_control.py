import tkinter as tk
from tkinter import filedialog

def openImageSelector():
    #TK cria uma UI para abrir o file explorer, com o codigo abaixo essa janela é oculta
    root = tk.Tk()
    root.withdraw()

    #Abre explorador de arquivos
    image_path = filedialog.askopenfilename(initialdir = "/",
                                          title = "Selecione uma imagem",
                                          filetypes=[
                                                    ('Imagens', ('.jpg', '.jpeg')),
                                                    ('Todos os arquivos', '.*')
                                                ])
    return image_path