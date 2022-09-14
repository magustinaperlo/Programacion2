
import tkinter as tk

comando =""
def calcular():
    global comando
    if operacion.get() == 1:
        comando = "Suma"
        return comando
    elif operacion.get() == 2:
        comando = "Resta"
        return comando
    elif operacion.get() == 3:
        comando = "Multi"
        return comando
    elif operacion.get() == 4:
        comando = "Divi"
        return comando
def retornar(comando):
    if comando == "Suma":
        suma()
    elif comando == "Resta":
        restar()
    elif comando == "Multi":
        multi()
    elif comando == "Divi":
        divi()

def multi():
    if int(n1.get()) !=0 and int(n2.get()) !=0:
        result = int(n1.get())* int(n2.get())
        valor.set(result)
def divi():
    if int(n1.get()) !=0 and int(n2.get()) !=0:
        result = int(n1.get())/ int(n2.get())
        valor.set(result)
def suma():
   result = int(n1.get())+ int(n2.get())
   valor.set(result)
def restar():
    result = int(n1.get())- int(n2.get())
    valor.set(result)
def go():
    global comando
    retornar(comando)


ventana = tk.Tk()
ventana.title("calculadora ")

operacion = tk.IntVar()
n1 = tk.IntVar(value=0)
lbl1 = tk.Label(ventana,text="Numero 1").grid()
entr1 = tk.Entry(ventana,textvariable=n1).grid()

n2= tk.IntVar(value=0)
lbl2 = tk.Label(ventana,text="Numero 2").grid()
entry2 = tk.Entry(ventana,textvariable=n2).grid()


lblo = tk.Label(ventana,text="Operaciones").grid()
sumar = tk.Radiobutton(ventana,text="Sumar",command=calcular,variable=operacion,value=1)
resta = tk.Radiobutton(ventana,text="Restar",command=calcular,variable=operacion,value=2)
multiplicar = tk.Radiobutton(ventana,text="Multiplicacion",command=calcular,variable=operacion,value=3)
division = tk.Radiobutton(ventana,text="Dividir",command=calcular,variable=operacion,value=4)

sumar.grid(column=1, row=0)
resta.grid(column=1, row=1)
multiplicar.grid(column=1, row=2)
division.grid(column=1, row=3)



valor = tk.IntVar(value=0)
lbl3 = tk.Label(ventana,text="Resultado").grid()
entry3 = tk.Entry(ventana,textvariable=valor,state="readonly").grid()


btn = tk.Button(ventana,text="Calcular",command=go).grid()
ventana.mainloop()