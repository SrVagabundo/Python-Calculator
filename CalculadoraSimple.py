from tkinter import *

#Base
root = Tk()
root.title("Calculadora Simple")
root['bg'] = '#404040'
root.resizable(width=False, height=False)
icon = PhotoImage(file='img/symbol.png')
root.iconphoto(False, icon)
e = Entry(root, width=15, borderwidth=5, font=('Comfortaa', 35), bg='#606060', fg='#E2E2E2', relief='flat')

#Funciones
def click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)




#Definiendo

img1 = PhotoImage(file='img/boton1.png')
boton1 = Button(root, text="", pady=40, command=lambda:click(1), image=img1, borderwidth=0, bg='#404040')

img2 = PhotoImage(file='img/boton2.png')
boton2 = Button(root, text="2", pady=40, command=lambda:click(2), image=img2, borderwidth=0, bg='#404040')

img3 = PhotoImage(file='img/boton3.png')
boton3 = Button(root, text="3", pady=40, command=lambda:click(3), image=img3, borderwidth=0, bg='#404040')

img4 = PhotoImage(file='img/boton4.png')
boton4 = Button(root, text="4", pady=40, command=lambda:click(4), image=img4, borderwidth=0, bg='#404040')

img5 = PhotoImage(file='img/boton5.png')
boton5 = Button(root, text="5", pady=40, command=lambda:click(5), image=img5, borderwidth=0, bg='#404040')

img6 = PhotoImage(file='img/boton6.png')
boton6 = Button(root, text="6", pady=40, command=lambda:click(6), image=img6, borderwidth=0, bg='#404040')

img7 = PhotoImage(file='img/boton7.png')
boton7 = Button(root, text="7", pady=40, command=lambda:click(7), image=img7, borderwidth=0, bg='#404040')

img8 = PhotoImage(file='img/boton8.png')
boton8 = Button(root, text="8", pady=40, command=lambda:click(8), image=img8, borderwidth=0, bg='#404040')

img9 = PhotoImage(file='img/boton9.png')
boton9 = Button(root, text="9", pady=40, command=lambda:click(9), image=img9, borderwidth=0, bg='#404040')

img0 = PhotoImage(file='img/boton0.png')
boton0 = Button(root, text="0", pady=40, command=lambda:click(0), image=img0, borderwidth=0, bg='#404040')

imgEqual = PhotoImage(file='img/botonEqual.png')
botonIgual = Button(root, text="=", padx=85, width=195, borderwidth=0, bg='#404040', image=imgEqual, command=button_equal)

imgPlus = PhotoImage(file='img/botonAdd.png')
botonSuma = Button(root, text="0", pady=40, command=button_add, image=imgPlus, borderwidth=0, bg='#404040')

imgMinus = PhotoImage(file='img/botonMinus.png')
botonResta = Button(root, text="0", pady=40, command=button_subtract, image=imgMinus, borderwidth=0, bg='#404040')

imgDivide = PhotoImage(file='img/botonDivide.png')
botonDivid = Button(root, text="0", pady=40, command=button_divide, image=imgDivide, borderwidth=0, bg='#404040')

imgMult = PhotoImage(file='img/botonMult.png')
botonMult = Button(root, text="0", pady=40, command=button_multiply, image=imgMult, borderwidth=0, bg='#404040')

imgClear = PhotoImage(file='img/botonClear.png')
botonClear = Button(root, text='Clear', pady=40, width=424, image=imgClear, borderwidth=0, bg='#404040', command=lambda:button_clear())

#Colocando
e.grid(row=0, column=1, columnspan=4, padx=10, pady=20) 
boton1.grid(row=3, column=1, pady=10)
boton2.grid(row=3, column=2, pady=10)
boton3.grid(row=3, column=3, pady=10)
boton4.grid(row=2, column=1, pady=10)
boton5.grid(row=2, column=2, pady=10)
boton6.grid(row=2, column=3, pady=10)
boton7.grid(row=1, column=1, pady=10)
boton8.grid(row=1, column=2, pady=10)
boton9.grid(row=1, column=3, pady=10)
boton0.grid(row=4, column=1, pady=10)
botonIgual.grid(row=4, column=2, columnspan=2)
botonSuma.grid(row=1, column=4, pady=10)
botonResta.grid(row=2, column=4, pady=10)
botonMult.grid(row=3, column=4, pady=10)
botonDivid.grid(row=4, column=4, pady=10)
botonClear.grid(row=5, column=1, columnspan=4, padx=10, pady=10) 

root.mainloop()
