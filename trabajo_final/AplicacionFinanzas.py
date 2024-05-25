import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import numpy as np
import LoginFrame, PlanAhorroFrame, RegistroFrame, FinanzasFrame


class Usuario:
    def __init__(self, id, contraseña):
        self.id = id
        self.contraseña = contraseña
        self.ingresos = 0
        self.egresos = 0
        self.saldo = 0
        self.movimientos = []  # Lista para almacenar movimientos
        self.plan_ahorro = 0  # Plan de ahorro del usuario
        self.numero_cuotas = None  # Número de cuotas para el plan de ahorro

class AplicacionFinanzas:
    def __init__(self, root):
        self.usuarios_registrados = {
            "usuario1": Usuario("usuario1", "contraseña1"),
            "usuario2": Usuario("usuario2", "contraseña2")
        }
        self.root = root
        self.root.title("Gestión Financiera")
        self.usuario_actual = None

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=1, fill="both")

        self.login = LoginFrame.LoginFrame(self.notebook, self.verificar_credenciales, self.cerrar_sesion)
        self.registro = RegistroFrame.RegistroFrame(self.notebook, self.registrar_nuevo_usuario)
        self.finanzas = FinanzasFrame.FinanzasFrame(self.notebook, self.registrar_ingreso, self.registrar_egreso, self.mostrar_plan_ahorro)

    def verificar_credenciales(self):
        id_ingresado = self.login.entry_id.get()
        contraseña_ingresada = self.login.entry_contraseña.get()

        if id_ingresado in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_ingresado]
            if contraseña_ingresada == usuario.contraseña:
                self.usuario_actual = usuario
                self.mostrar_interfaz_finanzas(usuario)
                self.root.title(f"Gestión Financiera - Usuario: {id_ingresado}")
                self.login.boton_cerrar_sesion.config(state="normal")
                messagebox.showinfo("¡Ingreso exitoso!", f"Bienvenido, {id_ingresado}!")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.root.title("Gestión Financiera")
        self.login.label_usuario.config(text="Usuario actual: ")
        self.login.boton_cerrar_sesion.config(state="disabled")
        messagebox.showinfo("Sesión cerrada", "Sesión cerrada exitosamente.")

    def mostrar_interfaz_finanzas(self, usuario):
        self.login.frame_login.pack_forget()

        self.finanzas.label_saldo.config(text=f"Saldo actual: {usuario.saldo}")
        self.mostrar_movimientos(usuario.movimientos)
        
        self.plan_ahorro = PlanAhorroFrame.PlanAhorroFrame(self.notebook, usuario)
        self.finanzas.boton_plan_ahorro.config(command=lambda: self.mostrar_plan_ahorro(self.plan_ahorro))

    def registrar_nuevo_usuario(self):
        nuevo_id = self.registro.entry_nuevo_id.get()
        nueva_contraseña = self.registro.entry_nueva_contraseña.get()

        if nuevo_id and nueva_contraseña:
            if nuevo_id in self.usuarios_registrados:
                messagebox.showerror("Error", "El usuario ya existe")
            else:
                nuevo_usuario = Usuario(nuevo_id, nueva_contraseña)
                self.usuarios_registrados[nuevo_id] = nuevo_usuario
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        else:
            messagebox.showerror("Error", "Ingrese un ID y contraseña válidos")

    def registrar_ingreso(self):
        try:
            monto = simpledialog.askfloat("Registrar Ingreso", "Ingrese el monto del ingreso:")
            concepto = simpledialog.askstring("Concepto", "Ingrese el concepto del ingreso:")

            if monto is not None:
                if monto <= 0:
                    raise ValueError("El monto debe ser mayor que cero")
                self.usuario_actual.ingresos += monto
                self.usuario_actual.saldo += monto
                self.usuario_actual.movimientos.append((concepto, monto, 'Ingreso'))
                messagebox.showinfo("Éxito", f"Ingreso de {monto} registrado.")
                self.actualizar_saldo()
                self.mostrar_movimientos(self.usuario_actual.movimientos)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def registrar_egreso(self):
        try:
            monto = simpledialog.askfloat("Registrar Egreso", "Ingrese el monto del egreso:")
            concepto = simpledialog.askstring("Concepto", "Ingrese el concepto del egreso:")

            if monto is not None:
                if monto <= 0:
                    raise ValueError("El monto debe ser mayor que cero")
                if monto > self.usuario_actual.saldo:
                    raise ValueError("Fondos insuficientes")
                self.usuario_actual.egresos += monto
                self.usuario_actual.saldo -= monto
                self.usuario_actual.movimientos.append((concepto, monto, 'Egreso'))
                messagebox.showinfo("Éxito", f"Egreso de {monto} registrado.")
                self.actualizar_saldo()
                self.mostrar_movimientos(self.usuario_actual.movimientos)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_saldo(self):
        self.finanzas.label_saldo.config(text=f"Saldo actual: {self.usuario_actual.saldo}")

    def mostrar_movimientos(self, movimientos):
        self.finanzas.tabla_movimientos.delete(*self.finanzas.tabla_movimientos.get_children())
        for idx, (concepto, monto, tipo) in enumerate(movimientos, start=1):
            self.finanzas.tabla_movimientos.insert("", "end", text=str(idx), values=(concepto, monto, tipo))

    def mostrar_plan_ahorro(self, plan_ahorro_frame):
        monto_abono = simpledialog.askfloat("Plan de Ahorro", "Ingrese el monto para abonar al plan de ahorro:")
        if monto_abono is not None:
            if monto_abono > self.usuario_actual.saldo:
                messagebox.showerror("Error", "Fondos insuficientes para el abono al ahorro.")
            else:
                self.usuario_actual.saldo -= monto_abono
                self.usuario_actual.plan_ahorro += monto_abono
                self.usuario_actual.movimientos.append(("Abono a Plan de Ahorro", monto_abono, 'Ahorro'))
                self.actualizar_saldo()
                self.mostrar_movimientos(self.usuario_actual.movimientos)
                plan_ahorro_frame.actualizar_labels()
                messagebox.showinfo("Éxito", f"Abono de {monto_abono} al Plan de Ahorro registrado.")

        plan_ahorro_frame.actualizar_labels()

    def agregar_usuario(self, id, contraseña):
        if id not in self.usuarios_registrados:
            nuevo_usuario = Usuario(id, contraseña)
            self.usuarios_registrados[id] = nuevo_usuario
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        else:
            messagebox.showerror("Error", "El usuario ya existe.")

    def eliminar_usuario(self, id):
        if id in self.usuarios_registrados:
            del self.usuarios_registrados[id]
            messagebox.showinfo("Éxito", f"Usuario {id} eliminado correctamente.")
        else:
            messagebox.showerror("Error", "El usuario no existe.")

    def modificar_contraseña(self, id, nueva_contraseña):
        if id in self.usuarios_registrados:
            self.usuarios_registrados[id].contraseña = nueva_contraseña
            messagebox.showinfo("Éxito", "Contraseña modificada correctamente.")
        else:
            messagebox.showerror("Error", "El usuario no existe.")


