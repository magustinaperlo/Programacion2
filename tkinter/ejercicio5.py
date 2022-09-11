import tkinter as tk

def incrementar():
    result = int(entrada.get()) +1
    valor.set(result)
def restar():
    result = int(entrada.get()) -1
    valor.set(result)
def reset():
    valor.set(0)
ventana = tk.Tk()
ventana.title("Contador ")
valor = tk.IntVar(value=0)
label = tk.Label(ventana,text="Contador").pack()
boton2 = tk.Button(ventana,text="restar",command = restar).pack()
entrada = tk.Entry(ventana,textvariable=valor,state="readonly")
entrada.pack()
boton = tk.Button(ventana,text="incrementar",command = incrementar).pack()
btnrst = tk.Button(ventana,text="Reset",command = reset).pack()
ventana.mainloop()