import tkinter as tk
from pathlib import Path
import pygame

pygame.mixer.init()
arquivo_audio = Path(__file__).with_name("setembro-vai-entrar-o-grosso-lula.mp3")
pygame.mixer.music.load(str(arquivo_audio))

def mudar_texto(event):
    pygame.mixer.music.play()
    label.config(text="Reproduzindo áudio...")

janela = tk.Tk()
janela.title("Evento enter")
janela.geometry("700x500")
janela.configure(bg="#0e91e9")

label = tk.Label(
    janela,
    text="Pressione Enter para reproduzir o áudio",
    bg="#0cce6d", fg="#ffffff",
    font=("Arial", 12, "bold")
)
label.pack(pady=50)

janela.bind('<Return>', mudar_texto)

janela.mainloop()
