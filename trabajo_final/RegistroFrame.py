import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class RegistroFrame:
    def __init__(self, notebook, registrar_nuevo_usuario):
        self.frame_registro = tk.Frame(notebook)
        notebook.add(self.frame_registro, text="Registrar usuario")
        self.registrar_nuevo_usuario = registrar_nuevo_usuario

        self.label_nuevo_id = ttk.Label(self.frame_registro, text="Nuevo ID de usuario:")
        self.label_nueva_contraseña = ttk.Label(self.frame_registro, text="Nueva Contraseña:")
        self.entry_nuevo_id = ttk.Entry(self.frame_registro)
        self.entry_nueva_contraseña = ttk.Entry(self.frame_registro, show="*")
        self.boton_registro = ttk.Button(self.frame_registro, text="Registrar nuevo usuario", command=self.registrar_nuevo_usuario)

        self.label_nuevo_id.grid(row=0, column=0, padx=5, pady=5)
        self.label_nueva_contraseña.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nuevo_id.grid(row=0, column=1, padx=5, pady=5)
        self.entry_nueva_contraseña.grid(row=1, column=1, padx=5, pady=5)
        self.boton_registro.grid(row=2, columnspan=2, padx=5, pady=5)