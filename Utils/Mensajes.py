import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje(tipo, mensaje, titulo="Aviso"):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()

    if tipo == "info":
        messagebox.showinfo(titulo, mensaje, parent=root)
    elif tipo == "error":
        messagebox.showerror(titulo, mensaje, parent=root)
    elif tipo == "advertencia":
        messagebox.showwarning(titulo, mensaje, parent=root)
    elif tipo == "pregunta":
        resultado = messagebox.askyesno(titulo, mensaje, parent=root)
        root.destroy()
        return resultado
    else:
        messagebox.showinfo(titulo, mensaje, parent=root)

    root.destroy()