import tkinter as tk

tela = tk.Tk()
tela.title("Minha Tela primeira tela")
tela.geometry("600x300")
tela.configure(bg="#080000")

label = tk.Label(tela, text= "Ola mundo!", fg="#178fff"); label.pack(padx=50, pady=100, anchor="w")

tela.mainloop()