import tkinter as tk

def incrementar():
    result = int(entrada.get()) +1
    valor.set(result)
def restar():
    result = int(entrada.get()) -1
    valor.set(result)
ventana = tk.Tk()
ventana.title("Contador decreciente")
valor = tk.IntVar(value=88)
label = tk.Label(ventana,text="Contador").pack()
boton2 = tk.Button(ventana,text="-",command = restar).pack()
entrada = tk.Entry(ventana,textvariable=valor,state="readonly")
entrada.pack()
boton = tk.Button(ventana,text="+",command = incrementar).pack()
ventana.mainloop()