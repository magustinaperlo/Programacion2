import tkinter as tk

def incrementar():
    result = int(entrada.get()) +1
    valor.set(result)
    
ventana = tk.Tk()
ventana.title("Contador")
#para que se pueda ver el contenido te agrego dimesiones especificas de la ventana
ventana.geometry("300x160")
valor = tk.IntVar()
label = tk.Label(ventana,text="Contador").pack()
entrada = tk.Entry(ventana,textvariable=valor,state="readonly")
entrada.pack()
boton = tk.Button(ventana,text="+",command = incrementar).pack()
ventana.mainloop()





