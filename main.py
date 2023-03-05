import tkinter as tk
from tkinter import ttk
from ventana_principal import VentanaPrincipal
class VentanaInicio(ttk.Frame):
    """Primera ventana que verá el usuario cuando inicie el programa"""
    def __init__(self,parent):
        """Se colocan todos los elementos de la ventana"""
        self.parent = parent
        ttk.Label(self.parent,text="Agenda en Python").grid(row=0,column=0)

        self.entrar_button = ttk.Button(self.parent,text="Entrar",command=self.ventana_principal)
        self.entrar_button.grid(row=1,column=1)

        self.salr_button = ttk.Button(self.parent, text="Salir")
        self.salr_button.grid(row=2, column=1)

        ttk.Label(self.parent,text="Copyright").grid(row=2,column=2)


    def ventana_principal(self):
        """Metodo que destruye la ventana actual para llevarnos a la ventana principal"""
        self.parent.destroy()
        VentanaPrincipal.ventana(self)





root = tk.Tk()
VentanaInicio(root)
root.mainloop()
