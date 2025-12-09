import tkinter as tk
from tkinter import messagebox


def pedir_confirmacion(mensaje, titulo="Confirmación"):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()
    resultado = messagebox.askyesno(
        title=titulo,
        message=mensaje,
        parent=root
    )
    root.destroy()
    return resultado