from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Importação de imagem")
app.geometry("400x400")

img_pill = Image.open(Path(__file__).resolve().with_name("skyrimfoto.png"))
img_pill = img_pill.resize((300, 300))

image_tk = ImageTk.PhotoImage(img_pill)

lbl_img = tk.Label(app, image=image_tk)
lbl_img.image = image_tk
lbl_img.pack(pady=20)

app.mainloop()