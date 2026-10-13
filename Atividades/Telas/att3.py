import tkinter as tk

janela = tk.Tk()
janela.title("Botão personalizado")
janela.geometry("720x1280")
janela.configure(bg="#8E57C5")

cor_alterada = False

def mudar_cor():
    global cor_alterada
    cor_alterada = not cor_alterada
    cor = "#29aabb" if cor_alterada else "#8E57C5"
    janela.configure(bg=cor)

btn = tk.Button(
    janela,
    text="Clique aqui",
    bg="#663399",
    fg="#f2ecf9",
    font=("Arial", 12, "bold"),
    command=mudar_cor
    
)

btn.place(relx=0.5, rely=0.5, anchor="center")
janela.mainloop()