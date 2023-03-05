import sqlite3

class BaseDatos:

    def crear_base_datos(self):
        self.conexion = sqlite3.connect("agenda.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS AGENDA (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        TITULO TEXT,
        FECHA TEXT,
        HORA TEXT,
        DURACION INTEGER,
        IMPORTANCIA TEXT,
        DESCRIPCION TEXT,
        ETIQUETAS TEXT,
        RECORDATORIO TEXT,
        DIA INTEGER,
        MES INTEGER,
        YEAR INTEGER,
        CODIGO INTEGER)""")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos(self, titulo,fecha,hora,duracion,importancia,descripcion,etiquetas,recordatorio,dia,mes,year,codigo):
        self.conexion = sqlite3.connect("agenda.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO AGENDA VALUES (NULL,'{titulo}','{fecha}','{hora}',{duracion},'{importancia}'"
                            f",'{descripcion}','{etiquetas}','{recordatorio}',{dia},{mes},{year},{codigo})")
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos(self,titulo,fecha,hora,duracion,importancia,descripcion,etiquetas,recordatorio):
        self.conexion = sqlite3.connect("agenda.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM AGENDA")
        self.cursor.execute(f"UPDATE AGENDA"
                            f"SET TITULO = '{titulo}', SET FECHA = '{fecha}', SET HORA = '{hora}', SET DURACION = {duracion}, SET IMPORTANCIA = '{importancia}',"
                            f"SET DESCRIPCION = '{descripcion}', SET ETIQUETAS = '{etiquetas}', SET RECORDATORIO = '{recordatorio}';")
        self.conexion.commit()
        self.conexion.close()


    def eliminar_datos(self,codigo):
        self.conexion = sqlite3.connect("agenda.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM AGENDA")
        self.cursor.execute(f"DELETE FROM AGENDA WHERE CODIGO = {codigo}")
        self.conexion.commit()
        self.conexion.close()