import tkinter as tk

def incrementar():
    result = int(entrada.get()) +1
    valor.set(result)
    
ventana = tk.Tk()
ventana.title("Contador")
valor = tk.IntVar()
label = tk.Label(ventana,text="Contador").pack()
entrada = tk.Entry(ventana,textvariable=valor,state="readonly")
entrada.pack()
boton = tk.Button(ventana,text="+",command = incrementar).pack()
ventana.mainloop()





