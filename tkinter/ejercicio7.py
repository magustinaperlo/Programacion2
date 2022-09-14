import tkinter as tk

def agregar():
    valor = entr1.get()
    cantidad = lista.size()
    lista.insert(cantidad,valor)
ventana = tk.Tk()
ventana.title("Peliculas ")
lbl = tk.Label(ventana,text="Ingresar pelicula").grid()
entr1 = tk.Entry(ventana)
entr1.grid()

lista = tk.Listbox(ventana)
lista.grid()

#   Botones
btn = tk.Button(ventana,text="Añadir",command=agregar).grid()
ventana.mainloop()