import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import numpy as np


class PlanAhorroFrame:
    def __init__(self, notebook, usuario):
        self.frame = tk.Frame(notebook)
        notebook.add(self.frame, text="Plan de Ahorro")
        self.usuario = usuario
        self.meta = np.inf  # Valor de la meta de ahorro

        self.label_ahorro = ttk.Label(self.frame, text="Total ahorrado: 0")
        self.label_meta = ttk.Label(self.frame, text=f"Meta de ahorro: {self.meta}")
        self.label_felicitacion = ttk.Label(self.frame, text="")
        self.entry_meta = ttk.Entry(self.frame)
        self.entry_abono = ttk.Entry(self.frame)
        self.boton_fijar_meta = ttk.Button(self.frame, text="Fijar Meta", command=self.fijar_meta)

        self.actualizar_labels()

        self.label_ahorro.pack()
        self.label_meta.pack()
        self.label_felicitacion.pack()
        self.entry_meta.pack()
        self.boton_fijar_meta.pack()

    def fijar_meta(self):
        self.meta = float(self.entry_meta.get())
        self.label_meta.config(text=f"Meta de ahorro: {self.meta}")
        self.mostrar_mensaje_felicitacion()

    def mostrar_plan_ahorro(self):
        monto_abono = simpledialog.askfloat("Plan de Ahorro", "Ingrese el monto para abonar al plan de ahorro:")
        if monto_abono is not None:
            if monto_abono > self.usuario.plan_ahorro:
                messagebox.showerror("Error", "Fondos insuficientes para el abono al ahorro.")
            else:
                self.usuario.saldo -= monto_abono
                self.usuario.plan_ahorro += monto_abono
                self.usuario.movimientos.append(("Abono a Plan de Ahorro", monto_abono, 'Ahorro'))
                self.actualizar_labels()

    def actualizar_labels(self):
        self.label_ahorro.config(text=f"Total ahorrado: {self.usuario.plan_ahorro}")
        self.mostrar_mensaje_felicitacion()

    def mostrar_mensaje_felicitacion(self):
        if self.usuario.plan_ahorro >= self.meta:
            self.label_felicitacion.config(text="¡Felicidades! ¡Has alcanzado tu meta de ahorro!")
