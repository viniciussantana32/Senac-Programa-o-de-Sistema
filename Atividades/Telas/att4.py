import tkinter as tk
from tkinter import ttk

class TelaOrigem(ttk.Frame):
    def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller

ttk.Label(self, text="Valor: ").pack(pady=5)
self.ent_val = ttk.Entry(self)
self.ent_val.insert(0, "250.00")
self.ent_val.pack(pady=5)

btn = ttk.Button(self, text="Enviar",
command=self.enviar)
btn.pack(pady=5)

def enviar(self):
    val = self.ent_val.get()

    self.controller.navegar("Destino", val)

class TelaDestino(tt.Frame):
    def __init__(self, parent, controller):
    super().__init__(parent)
    self.lbl = ttk.Label(self, text="")
    self.lbl.pack.(pady=20)

def receber_dados(self, valor):

    self.lbl.config(text=f"Recebido: R${valor}")

class App(tk.Tk):
    def navegar(self, nome_tel, dado):
        tela = self.telas[nome_tela]
        if