import calendar
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import *
class VentanaPrincipal:

    def ventana(self):
        self.root = tk.Tk()
        now = datetime.now()
        ttk.Label(self.root,text=f"Hoy es {now.day}/{now.month}/{now.year}").grid(row=0,column=0)

        cal = Calendar(self.root,selectmode="day",year=now.year,month=now.month, day=now.day,locale="es")
        cal.grid(row=1,column=0)
        self.vista_button = tk.Button(self.root, text="Vista Semanal/Mensual")
        self.vista_button.grid(row=2, column=0)

        self.busqueda = tk.StringVar()
        self.buscador_input = tk.Entry(self.root,textvariable=self.busqueda)
        self.buscador_input.grid(row=3,column=0)
        self.buscador_button = tk.Button(self.root,text="Buscar")
        self.buscador_button.grid(row=3,column=1)

        self.root.mainloop()

    def tabla_treeview(self):
        self.tabla = ttk.Treeview(self.root, height=16,
                                  columns=("#1", "#2", "#3", "#4", "#5"))
        self.tabla.place(relx=0,rely=0)

        self.tabla.column("#1", width=80, anchor="CENTER")
        self.tabla.column("#2", width=80, anchor="CENTER")
        self.tabla.column("#3", width=80, anchor="CENTER")
        self.tabla.column("#4", width=80, anchor="CENTER")
        self.tabla.column("#5", width=80, anchor="CENTER")

        self.tabla["show"] = "headings"
        self.tabla.heading("#1", text="TITULO", anchor="CENTER")
        self.tabla.heading("#2", text="FECHA", anchor="CENTER")
        self.tabla.heading("#3", text="DESDE", anchor="CENTER")
        self.tabla.heading("#4", text="HASTA", anchor="CENTER")
        self.tabla.heading("#5", text="DESCRIPCION", anchor="CENTER")




