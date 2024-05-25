import tkinter as tk
from tkinter import ttk

class FinanzasFrame:
    def __init__(self, notebook, registrar_ingreso, registrar_egreso, mostrar_plan_ahorro):
        self.frame_finanzas = tk.Frame(notebook)
        self.registrar_ingreso = registrar_ingreso
        self.registrar_egreso = registrar_egreso
        self.mostrar_plan_ahorro = mostrar_plan_ahorro
        notebook.add(self.frame_finanzas, text="Gestión Financiera")

        self.label_saldo = ttk.Label(self.frame_finanzas, text="Saldo actual: 0")
        self.boton_registrar_ingreso = ttk.Button(self.frame_finanzas, text="Registrar Ingreso", command=self.registrar_ingreso)
        self.boton_registrar_egreso = ttk.Button(self.frame_finanzas, text="Registrar Egreso", command=self.registrar_egreso)
        self.boton_plan_ahorro = ttk.Button(self.frame_finanzas, text="Establecer Plan de Ahorro", command=self.mostrar_plan_ahorro)
        self.tabla_movimientos = ttk.Treeview(self.frame_finanzas)

        self.label_saldo.grid(row=0, column=0, padx=10, pady=10)
        self.boton_registrar_ingreso.grid(row=1, column=0, padx=10, pady=5)
        self.boton_registrar_egreso.grid(row=2, column=0, padx=10, pady=5)
        self.boton_plan_ahorro.grid(row=3, column=0, padx=10, pady=5)
        self.tabla_movimientos.grid(row=4, column=0, padx=10, pady=5)

        self.tabla_movimientos['columns'] = ('concepto', 'monto', 'tipo')
        self.tabla_movimientos.column('#0', width=0, stretch=tk.NO)
        self.tabla_movimientos.column('concepto', anchor=tk.W, width=200)
        self.tabla_movimientos.column('monto', anchor=tk.CENTER, width=100)
        self.tabla_movimientos.column('tipo', anchor=tk.W, width=100)
        self.tabla_movimientos.heading('#0', text='', anchor=tk.W)
        self.tabla_movimientos.heading('concepto', text='Concepto', anchor=tk.W)
        self.tabla_movimientos.heading('monto', text='Monto', anchor=tk.CENTER)
        self.tabla_movimientos.heading('tipo', text='Tipo', anchor=tk.W)