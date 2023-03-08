import calendar
import tkinter as tk
from tkinter import ttk, CENTER,messagebox
from datetime import datetime
from tkcalendar import *
from base_datos import BaseDatos
import sqlite3

class VentanaPrincipal:

    def __init__(self):
        self.ventana()

    def ventana(self):
        self.root = tk.Tk()
        now = datetime.now()
        ttk.Label(self.root,text=f"Hoy es {now.day}/{now.month}/{now.year}").grid(row=0,column=0)

        cal = Calendar(self.root,selectmode="day",year=now.year,month=now.month, day=now.day,locale="es")
        cal.grid(row=1,column=0)
        self.vista_button = ttk.Button(self.root, text="Vista Semanal/Mensual")
        self.vista_button.grid(row=2, column=0)

        self.busqueda = tk.StringVar()
        self.buscador_input = ttk.Entry(self.root,textvariable=self.busqueda)
        self.buscador_input.grid(row=3,column=0)
        self.buscador_button = ttk.Button(self.root,text="Buscar")
        self.buscador_button.grid(row=3,column=1)
        self.retroceder_button = ttk.Button(self.root,text="Retroceder")
        self.retroceder_button.grid(row=4,column=1)
        self.siguiente_button = ttk.Button(self.root, text="Siguiente")
        self.siguiente_button.grid(row=5, column=1)
        self.agregar_evento_button = ttk.Button(self.root, text="Agregar Evento",
                                                command=self.agregar_o_modificar_evento_ventana)
        self.agregar_evento_button.grid(row=6,column=1)
        self.modificar_evento_button = ttk.Button(self.root, text="Modificar Evento")
        self.modificar_evento_button.grid(row=7, column=1)
        self.eliminar_evento_button = ttk.Button(self.root, text="Eliminar Evento")
        self.eliminar_evento_button.grid(row=8, column=1)
        self.salir_button = ttk.Button(self.root, text="Salir")
        self.salir_button.grid(row=9, column=1)
        self.tabla_treeview()

        self.root.mainloop()

    def tabla_treeview(self):
        self.tabla_contenedor = ttk.Frame(self.root)
        self.tabla_contenedor.grid(row=0,column=2,columnspan=3,rowspan=3)
        self.tabla = ttk.Treeview(self.tabla_contenedor, height=15,
                                  columns=("#1", "#2", "#3", "#4", "#5"))
        self.tabla.pack()

        self.tabla.column("#1", width=100, anchor=CENTER)
        self.tabla.column("#2", width=80, anchor=CENTER)
        self.tabla.column("#3", width=80, anchor=CENTER)
        self.tabla.column("#4", width=80, anchor=CENTER)
        self.tabla.column("#5", width=160, anchor=CENTER)

        self.tabla["show"] = "headings"
        self.tabla.heading("#1", text="TITULO", anchor=CENTER)
        self.tabla.heading("#2", text="FECHA", anchor=CENTER)
        self.tabla.heading("#3", text="DESDE", anchor=CENTER)
        self.tabla.heading("#4", text="HASTA", anchor=CENTER)
        self.tabla.heading("#5", text="DESCRIPCION", anchor=CENTER)


        self.base_de_datos = BaseDatos()
        self.base_de_datos.crear_base_datos()
        self.conexion = sqlite3.connect("agenda.db")
        self.cursor = self.conexion.cursor()
        self.insertar = self.cursor.execute("SELECT * FROM AGENDA")
        for dato in self.insertar:
            self.tabla.insert('', 0, values=(dato[0], dato[1], dato[2], dato[3],dato[5]))
        self.conexion.commit()
        self.conexion.close()

    def agregar_o_modificar_evento_ventana(self,label,comando):
        self.root.destroy()
        self.evento_ventana = tk.Tk()
        ttk.Label(self.evento_ventana,text=label).pack
        ttk.Label(self.evento_ventana,text="Titulo").pack()
        self.titulo_entry = ttk.Entry(self.evento_ventana)
        self.titulo_entry.pack()

        ttk.Label(self.evento_ventana,text="Fecha").pack()
        self.fecha_entry = ttk.Entry(self.evento_ventana)
        self.fecha_entry.pack()

        ttk.Label(self.evento_ventana,text="Hora Inicio").pack()
        self.hora_entry = ttk.Entry(self.evento_ventana)
        self.hora_entry.pack()

        ttk.Label(self.evento_ventana,text="Hora Finalizacion").pack()
        self.hora_salida_entry = ttk.Entry(self.evento_ventana)
        self.hora_salida_entry.pack()

        ttk.Label(self.evento_ventana, text="Importancia").pack()
        self.importancia_value = tk.StringVar()
        self.importancia_entry = ttk.Combobox(self.evento_ventana,values=["Normal","Importante"],
                                              textvariable=self.importancia_value,state="readonly")
        self.importancia_entry.pack()

        ttk.Label(self.evento_ventana, text="Descripcion").pack()
        self.descripcion_entry = ttk.Entry(self.evento_ventana)
        self.descripcion_entry.pack()

        ttk.Label(self.evento_ventana, text="Etiquetas").pack()
        self.etiquetas_entry = ttk.Entry(self.evento_ventana)
        self.etiquetas_entry.pack()

        self.cancelar_button = ttk.Button(self.evento_ventana,text="Cancelar")
        self.cancelar_button.pack()

        self.aceptar_button = ttk.Button(self.evento_ventana, text="Aceptar", command=comando)
        self.aceptar_button.pack()

        self.evento_ventana.mainloop()


    def validacion_datos(self):
        return not self.titulo_entry.get() or not self.fecha_entry.get() or not self.hora_entry.get() \
            or self.importancia_value == "" or not self.hora_salida_entry.get() or not self.etiquetas_entry.get()

    def enviar_datos(self):
        if self.validacion_datos() == True:
            messagebox.showerror(message="No debe dejar campos vacios")
        else:
          pass


VentanaPrincipal()