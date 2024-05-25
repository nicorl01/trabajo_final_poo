import tkinter as tk
from tkinter import ttk
class LoginFrame:
    def __init__(self, notebook, verificar_credenciales, cerrar_sesion):
        self.verificar_credenciales = verificar_credenciales
        self.cerrar_sesion = cerrar_sesion
        self.notebook = notebook
        self.frame_login = tk.Frame(notebook)
        notebook.add(self.frame_login, text="Login")

        self.label_usuario = ttk.Label(self.frame_login, text="Usuario actual: ")
        self.label_id = ttk.Label(self.frame_login, text="ID de usuario:")
        self.label_contraseña = ttk.Label(self.frame_login, text="Contraseña:")
        self.entry_id = ttk.Entry(self.frame_login)
        self.entry_contraseña = ttk.Entry(self.frame_login, show="*")
        self.boton_login = ttk.Button(self.frame_login, text="Iniciar sesión", command=self.verificar_credenciales)
        self.boton_cerrar_sesion = ttk.Button(self.frame_login, text="Cerrar sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.config(state="disabled")

        self.label_usuario.grid(row=0, columnspan=2, padx=5, pady=5, sticky="w")
        self.label_id.grid(row=1, column=0, padx=5, pady=5)
        self.label_contraseña.grid(row=2, column=0, padx=5, pady=5)
        self.entry_id.grid(row=1, column=1, padx=5, pady=5)
        self.entry_contraseña.grid(row=2, column=1, padx=5, pady=5)
        self.boton_login.grid(row=3, columnspan=2, padx=5, pady=5)
        self.boton_cerrar_sesion.grid(row=4, columnspan=2, padx=5, pady=5)