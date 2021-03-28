from tkinter import *

#Base
root = Tk()
root.title("Calculadora Simple")
root['bg'] = '#404040'
root.resizable(width=False, height=False)

#Funciones
def suma():
    return

#Definiendo
entrada = Entry(root, width=70, borderwidth=5)
entrada.insert(0, "")

img1 = PhotoImage(file='img/boton1.png')
boton1 = Button(root, text="", padx=35, pady=20, command=suma, image=img1, borderwidth=0, bg='#404040')

img2 = PhotoImage(file='img/boton2.png')
boton2 = Button(root, text="2", padx=35, pady=20, command=suma, image=img2, borderwidth=0, bg='#404040')

img3 = PhotoImage(file='img/boton3.png')
boton3 = Button(root, text="3", padx=35, pady=20, command=suma, image=img3, borderwidth=0, bg='#404040')

img4 = PhotoImage(file='img/boton4.png')
boton4 = Button(root, text="4", padx=35, pady=20, command=suma, image=img4, borderwidth=0, bg='#404040')

img5 = PhotoImage(file='img/boton5.png')
boton5 = Button(root, text="5", padx=35, pady=20, command=suma, image=img5, borderwidth=0, bg='#404040')

img6 = PhotoImage(file='img/boton6.png')
boton6 = Button(root, text="6", padx=35, pady=20, command=suma, image=img6, borderwidth=0, bg='#404040')

img7 = PhotoImage(file='img/boton7.png')
boton7 = Button(root, text="7", padx=35, pady=20, command=suma, image=img7, borderwidth=0, bg='#404040')

img8 = PhotoImage(file='img/boton8.png')
boton8 = Button(root, text="8", padx=35, pady=20, command=suma, image=img8, borderwidth=0, bg='#404040')

img9 = PhotoImage(file='img/boton9.png')
boton9 = Button(root, text="9", padx=35, pady=20, command=suma, image=img9, borderwidth=0, bg='#404040')

img0 = PhotoImage(file='img/boton0.png'),
boton0 = Button(root, text="0", padx=35, pady=20, command=suma, image=img0, borderwidth=0, bg='#404040')

imgEqual = PhotoImage(file='img/botonEqual.png')
botonIgual = Button(root, text="=", padx=77, pady=21, image=imgEqual, borderwidth=0, bg='#404040')

imgPlus = PhotoImage(file='img/boton0.png'),
botonSuma = Button(root, text="0", padx=35, pady=20, command=suma, image=img0, borderwidth=0, bg='#404040')

imgMinus = PhotoImage(file='img/boton0.png'),
botonResta = Button(root, text="0", padx=35, pady=20, command=suma, image=img0, borderwidth=0, bg='#404040')

imgDivide = PhotoImage(file='img/boton0.png'),
botonDivid = Button(root, text="0", padx=35, pady=20, command=suma, image=img0, borderwidth=0, bg='#404040')

imgMult = PhotoImage(file='img/boton0.png'),
botonMult = Button(root, text="0", padx=35, pady=20, command=suma, image=img0, borderwidth=0, bg='#404040')

#Colocando
entrada.grid(row=0, column=1, columnspan=4, padx=10, pady=20)
boton1.grid(row=3, column=1)
boton2.grid(row=3, column=2)
boton3.grid(row=3, column=3)
boton4.grid(row=2, column=1)
boton5.grid(row=2, column=2)
boton6.grid(row=2, column=3)
boton7.grid(row=1, column=1)
boton8.grid(row=1, column=2)
boton9.grid(row=1, column=3)
boton0.grid(row=4, column=1)
botonIgual.grid(row=4, column=2, columnspan=2)
botonSuma.grid(row=1, column=4)
botonResta.grid(row=2, column=4)
botonMult.grid(row=3, column=4)
botonDivid.grid(row=4, column=4)

root.mainloop()