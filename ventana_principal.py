import calendar
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import *
class VentanaPrincipal:

    def ventana(self):
        root = tk.Tk()
        now = datetime.now()
        ttk.Label(root,text=f"Hoy es {now.day}/{now.month}/{now.year}").grid(row=0,column=0)

        cal = Calendar(root,selectmode="day",year=now.year,month=now.month, day=now.day,locale="es")
        cal.grid(row=1,column=0)

        print(cal.get_date())

        root.mainloop()



