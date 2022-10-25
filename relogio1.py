# Importação bibliotecas para data e tempo
from distutils.text_file import TextFile
from tkinter import *
import tkinter
from datetime import datetime

# Importação para adicionar fonte
import pyglet
pyglet.font.add_file("digital-7.ttf")

# Ccores para alterar
cor1 = "#3d3d3d"  # Preta
cor2 = "#fafcff"  # Branca
cor3 = "#21c25c"  # Verde
cor4 = "#eb463b"  # Vermelho

background = cor1
fontes = cor2

# Janela da aplicação
janela = Tk()
janela.title("")
janela.geometry("420x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


def relogio():  # Método de data e hora
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")  # %B maiusculo irá dar completo do mes
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=semana + "          " + str(dia) +
              " / " + str(mes) + " / " + str(ano))

# Labels tkinter
l1 = Label(janela, text="", font=("digital-7 100"), bg=background, fg=fontes)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(janela, text="", font=("digital-7 20"), bg=background, fg=fontes)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()
