from tkinter import *

#Base
root = Tk()
root.title("Calculadora Simple")
#Funciones
def suma():
    return

#Definiendo
entrada = Entry(root, width=35, borderwidth=5)
entrada.insert(0, "")
boton1 = Button(root, text="1", padx=35, pady=20, command=suma)
boton2 = Button(root, text="2", padx=35, pady=20, command=suma)
boton3 = Button(root, text="3", padx=35, pady=20, command=suma)
boton4 = Button(root, text="4", padx=35, pady=20, command=suma)
boton5 = Button(root, text="5", padx=35, pady=20, command=suma)
boton6 = Button(root, text="6", padx=35, pady=20, command=suma)
boton7 = Button(root, text="7", padx=35, pady=20, command=suma)
boton8 = Button(root, text="8", padx=35, pady=20, command=suma)
boton9 = Button(root, text="9", padx=35, pady=20, command=suma)
boton0 = Button(root, text="0", padx=35, pady=20, command=suma)
botonIgual = Button(root, text="=", padx=77, pady=20)

#Colocando
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=20)
boton1.grid(row=3, column=0)
boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)
boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)
boton7.grid(row=1, column=0)
boton8.grid(row=1, column=1)
boton9.grid(row=1, column=2)
boton0.grid(row=4, column=0)
botonIgual.grid(row=4, column=1, columnspan=3)


root.mainloop()