from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("350x250")

img_pill = Image.open(Path(__file__).resolve().with_name("bottom-alignment.png"))
img_pill = img_pill.resize((24,24))

icone_tk = ImageTk.PhotoImage(img_pill)

btn = tk.Button(app, text="karai", image=icone_tk, compound="left")

btn.image = icone_tk
btn.pack(pady=40)
app.mainloop()