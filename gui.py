import BDVehiculo as bdv
import FBicicleta as fbi
import FCoche as fco
import FFurgoneta as ffu
import FQuad as fqu
import FMotocicleta as fmo
import helpers as hlp
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING




class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")



class Ventana_crear_vehiculo(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear vehiculo")
        self.center()
        self.config(bg="light green")
        self.build()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx = 20, pady = 20)

        Label(frame, text="Tipo de vehiculo").grid(row = 0, column = 0)
        self.tipo = ttk.Combobox(frame, values=["Bicicleta", "Coche", "Furgoneta", "Quad", "Motocicleta"])
        self.tipo.grid(row = 0, column = 1)
        self.tipo.bind("<<ComboboxSelected>>", self.on_tipo_selected)

        self.casillas = {}

        Button(frame, text="Crear", command=self.create).grid(row = 1, column = 0)
        Button(frame, text="Cancelar", command=self.close).grid(row = 1, column = 1)

    def on_tipo_selected(self, event):
        tipo = self.tipo.get()
        if tipo == "Bicicleta":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["2"]),
                "Precio": Entry(self),
                "Tipo": ttk.Combobox(self, values=["Montaña", "Ciudad", "Paseo", "BMX"])
            }
        elif tipo == "Coche":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["4"]),
                "Precio": Entry(self),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self)
            }
        elif tipo == "Furgoneta":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["4"]),
                "Precio": Entry(self),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self),
                "Carga": Entry(self)
            }
        elif tipo == "Motocicleta":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["2"]),
                "Precio": Entry(self),
                "Tipo": ttk.Combobox(self, values=["Turismo", "Deportiva", "Naked", "Enduro", "Chopper", "Custom"]),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self)

            }
        elif tipo == "Quad":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["4"]),
                "Precio": Entry(self),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self),
                "Tipo": ttk.Combobox(self, values=["Pesado", "Ligero"]),
                "Carga": Entry(self)

            }

        for i, (key, value) in enumerate(self.casillas.items()):
            Label(self, text=key).grid(row=i+2, column=0)
            value.grid(row=i+2, column=1)

    def create(self):
        tipo = self.tipo.get()
        if tipo == "Bicicleta":
            fbi.crear_bicicleta(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Tipo"].get())
        elif tipo == "Coche":
            fco.crear_coche(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get())
        elif tipo == "Furgoneta":
            ffu.crear_furgoneta(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get(), self.casillas["Carga"].get())
        elif tipo == "Motocicleta":
            fmo.crear_motocicleta(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Tipo"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get())
        elif tipo == "Quad":
            fqu.crear_quad(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get(), self.casillas["Tipo"].get(), self.casillas["Carga"].get())

    def close(self):
        self.destroy()
        self.update()


class Ventana_editar_vehiculo(Toplevel, CenterWidgetMixin):
    def __init__(self, parent, vehiculo):
        Toplevel.__init__(self, parent)
        self.title("Editar vehiculo")
        self.center()
        self.config(bg="light blue")
        self.build(vehiculo)
        self.transient(parent)
        self.grab_set()

    def build(self, vehiculo):
        frame = Frame(self)
        frame.pack(padx = 20, pady = 20)

        Label(frame, text="Tipo de vehiculo").grid(row = 0, column = 0)
        self.tipo = ttk.Combobox(frame, values=["Bicicleta", "Coche", "Furgoneta", "Quad", "Motocicleta"])
        self.tipo.grid(row = 0, column = 1)
        self.tipo.bind("<<ComboboxSelected>>", self.on_tipo_selected)

        self.casillas = {}

        Button(frame, text="Editar", command=self.edit).grid(row = 1, column = 0)
        Button(frame, text="Cancelar", command=self.close).grid(row = 1, column = 1)

    def on_tipo_selected(self, event):
        tipo = self.tipo.get()
        if tipo == "Bicicleta":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["2"]),
                "Precio": Entry(self),
                "Tipo": ttk.Combobox(self, values=["Montaña", "Ciudad", "Paseo", "BMX"])
            }
        elif tipo == "Coche":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["4"]),
                "Precio": Entry(self),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self)
            }
        elif tipo == "Furgoneta":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["4"]),
                "Precio": Entry(self),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self),
                "Carga": Entry(self)
            }
        elif tipo == "Motocicleta":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["2"]),
                "Precio": Entry(self),
                "Tipo": ttk.Combobox(self, values=["Turismo", "Deportiva", "Naked", "Enduro", "Chopper", "Custom"]),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self)

            }
        elif tipo == "Quad":
            self.casillas = {
                "Modelo": Entry(self),
                "Vehiculo": Entry(self),
                "Marca": Entry(self),
                "Color": Entry(self),
                "Ruedas": Entry(self, values = ["4"]),
                "Precio": Entry(self),
                "Velocidad": Entry(self),
                "Cilindrada": Entry(self),
                "Tipo": ttk.Combobox(self, values=["Pesado", "Ligero"]),
                "Carga": Entry(self)

            }

        for i, key in enumerate(self.casillas):
            Label(self, text=key).grid(row = i + 2, column = 0)
            self.casillas[key].grid(row = i + 2, column = 1)

        vehiculo = self.master.treeview.focus()
        values = self.master.treeview.item(vehiculo, "values")
        self.casillas["Modelo"].insert(0, values[0])
        self.casillas["Vehiculo"].insert(0, values[1])
        self.casillas["Marca"].insert(0, values[2])
        self.casillas["Color"].insert(0, values[3])
        self.casillas["Ruedas"].insert(0, values[4])
        self.casillas["Precio"].insert(0, values[5])
        if tipo == "Bicicleta":
            self.casillas["Tipo"].insert(0, values[6])
        elif tipo == "Coche":
            self.casillas["Velocidad"].insert(0, values[6])
            self.casillas["Cilindrada"].insert(0, values[7])
        elif tipo == "Furgoneta":
            self.casillas["Velocidad"].insert(0, values[6])
            self.casillas["Cilindrada"].insert(0, values[7])
            self.casillas["Carga"].insert(0, values[8])
        elif tipo == "Motocicleta":
            self.casillas["Tipo"].insert(0, values[6])
            self.casillas["Velocidad"].insert(0, values[7])
            self.casillas["Cilindrada"].insert(0, values[8])
        elif tipo == "Quad":
            self.casillas["Tipo"].insert(0, values[6])
            self.casillas["Velocidad"].insert(0, values[7])
            self.casillas["Cilindrada"].insert(0, values[8])
            self.casillas["Carga"].insert(0, values[9])
            
    def edit(self):
        tipo = self.tipo.get()
        if tipo == "Bicicleta":
            fbi.editar_bicicleta(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Tipo"].get())
        elif tipo == "Coche":
            fco.editar_coche(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get())
        elif tipo == "Furgoneta":
            ffu.editar_furgoneta(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get(), self.casillas["Carga"].get())
        elif tipo == "Motocicleta":
            fmo.editar_motocicleta(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Tipo"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get())
        elif tipo == "Quad":
            fqu.editar_quad(self.casillas["Modelo"].get(), self.casillas["Vehiculo"].get(), self.casillas["Marca"].get(), self.casillas["Color"].get(), self.casillas["Ruedas"].get(), self.casillas["Precio"].get(), self.casillas["Velocidad"].get(), self.casillas["Cilindrada"].get(), self.casillas["Tipo"].get(), self.casillas["Carga"].get())

    def close(self):
        self.destroy()
        self.update()


class Ventana_eliminar_vehiculo(Toplevel):
    def __init__(self, master, tipo):
        super().__init__(master)
        self.master = master
        self.tipo = tipo
        self.title("Eliminar")
        self.geometry("300x200")
        self.resizable(False, False)
        self.config(bg = "white")
        self.grab_set()
        self.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.init_gui()

    def init_gui(self):
        Label(self, text = "¿Estás seguro de que quieres eliminar este vehículo?", bg = "white").pack(pady = 10)
        Button(self, text = "Si", command = self.delete).pack(pady = 10)
        Button(self, text = "No", command = self.close).pack(pady = 10)

    def delete(self):
        tipo = self.tipo.get()
        if tipo == "Bicicleta":
            fbi.eliminar_bicicleta(self.master.treeview.focus())
        elif tipo == "Coche":
            fco.eliminar_coche(self.master.treeview.focus())
        elif tipo == "Furgoneta":
            ffu.eliminar_furgoneta(self.master.treeview.focus())
        elif tipo == "Motocicleta":
            fmo.eliminar_motocicleta(self.master.treeview.focus())
        elif tipo == "Quad":
            fqu.eliminar_quad(self.master.treeview.focus())
        self.destroy()
        self.update()

    def close(self):
        self.destroy()
        self.update()


class Ventana_principal(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Vehículos")
        self.geometry("800x600")
        self.resizable(1, 1)
        self.config(bg = "white")
        self.init_gui()

    def init_gui(self):
        frame = Frame(self, bg = "white")
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview["columns"] = ("Modelo", "Vehiculo", "Marca", "Color", "Ruedas", "Precio", "Tipo", "Velocidad", "Cilindrada", "Carga")

        treeview.column("#0", width = 0, stretch = NO)
        treeview.column("Modelo", anchor = CENTER, width = 100)
        treeview.column("Vehiculo", anchor = CENTER, width = 100)
        treeview.column("Marca", anchor = CENTER, width = 100)
        treeview.column("Color", anchor = CENTER, width = 100)
        treeview.column("Ruedas", anchor = CENTER, width = 100)
        treeview.column("Precio", anchor = CENTER, width = 100)
        treeview.column("Tipo", anchor = CENTER, width = 100)
        treeview.column("Velocidad", anchor = CENTER, width = 100)
        treeview.column("Cilindrada", anchor = CENTER, width = 100)
        treeview.column("Carga", anchor = CENTER, width = 100)

        treeview.heading("Modelo", text = "Modelo", anchor = CENTER)
        treeview.heading("Vehiculo", text = "Vehiculo", anchor = CENTER)
        treeview.heading("Marca", text = "Marca", anchor = CENTER)
        treeview.heading("Color", text = "Color", anchor = CENTER)
        treeview.heading("Ruedas", text = "Ruedas", anchor = CENTER)
        treeview.heading("Precio", text = "Precio", anchor = CENTER)
        treeview.heading("Tipo", text = "Tipo", anchor = CENTER)
        treeview.heading("Velocidad", text = "Velocidad", anchor = CENTER)
        treeview.heading("Cilindrada", text = "Cilindrada", anchor = CENTER)
        treeview.heading("Carga", text = "Carga", anchor = CENTER)

        scrollbary = Scrollbar(frame)
        scrollbary.pack(side = RIGHT, fill = Y)
        treeview['yscrollcommand'] = scrollbary.set

        scrollbarx = Scrollbar(frame)
        scrollbarx.pack(side = BOTTOM, fill = X)
        treeview['xscrollcommand'] = scrollbarx.set

        for vhc in bdv.Vehiculos.lista:
            treeview.insert(parent="", index = 'end', id = vhc.get_modelo(), values = (vhc.get_modelo(), vhc.get_tipo(), vhc.get_marca(), vhc.get_color(), vhc.get_ruedas(), vhc.get_precio(), vhc.get_tipo(), vhc.get_velocidad(), vhc.get_cilindrada(), vhc.get_carga()))

        treeview.pack()

        frame =  Frame(self)
        frame.pack(pady = 20)

        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)

        self.treeview = treeview

    def create(self):
        Ventana_crear_vehiculo(self)

    def edit(self):
        Ventana_editar_vehiculo(self)

    def delete(self):
        Ventana_eliminar_vehiculo(self)


if __name__ == "__main__":
    app = Ventana_principal()
    app.mainloop()











        
   

            



            