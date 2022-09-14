import tkinter as tk

def incrementar():
    result = int(entrada.get()) -1
    valor.set(result)
    
ventana = tk.Tk()
ventana.title("Contador decreciente")
#agrego dimension de la ventana
ventana.geometry("300x160")
valor = tk.IntVar()
label = tk.Label(ventana,text="Contador").pack()
#debe inicializar en 88
entrada = tk.Entry(ventana,textvariable=valor,state="readonly")
entrada.pack()
boton = tk.Button(ventana,text="-",command = incrementar).pack()
ventana.mainloop()
