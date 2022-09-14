from os import stat
import tkinter as tk



ventana = tk.Tk()
ventana.title("Contador factorial")
ventana.resizable(False, False)
ventana.geometry("440x170")


def factor():
    num = int(valor1.get())+1
    con = 1
    result = 1
    while num != 0:
        result *= con
        valor2.set(result)
        valor1.set(con) 
        con +=1
        num -= 1
def factorfor():
    num = int(valor1.get())+1
    result = 1
    for x in range(num):
        result *= x+1
        valor2.set(result)
        valor1.set(x+1) 
        
        
    
valor1 = tk.IntVar(value=1)
valor2 = tk.IntVar(value=1)
label2 = tk.Label(ventana,text="N").pack()
entry = tk.Entry(ventana,textvariable=valor1,state="readonly")
entry.pack()
label = tk.Label(ventana,text="Factorial").pack()
boton2 = tk.Button(ventana,text="Factor while",command = factor).pack()
boton3 = tk.Button(ventana,text="Factor for",command = factorfor).pack()
entrada = tk.Entry(ventana,textvariable=valor2,state="readonly")
entrada.pack()

ventana.mainloop()
