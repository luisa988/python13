import tkinter as tk
from tkinter import ttk


def suma():
    num1= int(ent_caja.get())
    num2= int(ent_caja1.get())
    salida = str(num1 + num2)
    cadena.set(salida)

def resta():
    num1= int(ent_caja.get())
    num2= int(ent_caja1.get())
    salida = str(num1 - num2)
    cadena.set(salida)

def multi():
    num1= int(ent_caja.get())
    num2= int(ent_caja1.get())
    salida = str(num1 * num2)
    cadena.set(salida)

def divi():
    num1= int(ent_caja.get())
    num2= int(ent_caja1.get())
    salida = str(num1 / num2)
    cadena.set(salida)
    
root=tk.Tk()
cadena=tk.StringVar()
cadena.set("")
root.geometry("500x500")
root.title("Aplicacion Grupo 432")


lbl_msge = tk.Label(root,textvariable=cadena)
lbl_msge.place(x=50,y=50)

ent_caja = tk.Entry(root)
ent_caja.place(x=50,y=100)
ent_caja1 = tk.Entry(root)
ent_caja1.place(x=200,y=100)
ent_caja2 = tk.Entry(root)
ent_caja2.place(x=350,y=100)

btn_click = tk.Button(root,text="suma",command=lambda: suma())
btn_click.place(x=50,y=150)
btn_click = tk.Button(root,text="resta",command=lambda: resta())
btn_click.place(x=150,y=150)
btn_resta = tk.Button(root,text="multi",command=lambda: multi())
btn_resta.place(x=250,y=150)
btn_resta = tk.Button(root,text="divi",command=lambda: divi())
btn_resta.place(x=350,y=150)



root.mainloop()