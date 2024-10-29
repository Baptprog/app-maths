import matplotlib.pyplot as plt
from tkinter import *
from numpy import *

fen = Tk()
fen.title('Générateur de courbe')
# Éléments de la fenêtre
label = Label(fen, text='Générateur de courbe', fg='blue')
label.grid(row=0, columnspan=2)

label2 = Label(fen, text="Entrez l'intervalle x de la courbe et le nombre de points :")
label2.grid(row=1, column=0)

mini = Entry(fen, width=10)
mini.grid(row=1, column=1, padx=30, pady=50)

maxi = Entry(fen, width=10)
maxi.grid(row=1, column=2, padx=40, pady=50)

pts = Entry(fen, width=10)
pts.grid(row=1, column=3, padx=40, pady=50)

label3 = Label(fen, text="Entrez la fonction associée à la courbe (cos,sqt,pi...):")
label3.grid(row=2, column=0)

func = Entry(fen, width=30)
func.grid(row=2, column=1)

def generer():
    x = linspace(float(mini.get()), float(maxi.get()), int(pts.get()))
    y = eval(func.get())
    plt.plot(x, y)
    plt.show()

gen = Button(fen, text='Générer', fg='green', command=generer)
gen.grid(row=3, column=0)

bye = Button(fen, text='Quitter', fg='red', command=fen.destroy)
bye.grid(row=3, column=1)

fen.mainloop()
