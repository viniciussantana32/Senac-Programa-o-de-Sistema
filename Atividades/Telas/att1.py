import tkinter as tk


numero1 = int(input("digite um número: "))
numero2 = int(input("digite outro número: "))
janela = tk.Tk()
janela.title("Minha Janela")

janela.geometry(f"{numero1}x{numero2}")

conteudo = tk.Frame(janela)
conteudo.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(conteudo, text="Olá, Mundo!")
label.pack(pady=20)

cliques = 0

def ao_clicar():
    global cliques
    cliques += 1
    label.config(text="EAE GAY!")
    if cliques == 2:
        janela.destroy()

botao = tk.Button(conteudo, text="Clique aqui", command=ao_clicar)
botao.pack()

janela.mainloop()