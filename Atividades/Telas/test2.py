import tkinter as tk

def mudar_texto(event):
    label.config(text="Mensagem alterada!")

janela = tk.Tk()
janela.title("Evento enter")
janela.geometry("700x500")
janela.configure(bg="#0e91e9")

label = tk.Label(
    janela,
    text="Pressione Enter para mudar a mensagem",
    bg="#0cce6d", fg="#ffffff",
    font=("Arial", 12, "bold")
)
label.pack(pady=50)

janela.bind('<Return>', mudar_texto)

janela.mainloop()

