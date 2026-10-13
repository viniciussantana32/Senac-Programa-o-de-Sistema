import tkinter as tk


def calcular(operacao):
    try:
        n1 = float(entry_numero1.get())
        n2 = float(entry_numero2.get())

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            if n2 == 0:
                lbl_resultado.config(text="Não é possível dividir por zero.")
                return
            resultado = n1 / n2
        else:
            lbl_resultado.config(text="Operação inválida.")
            return

        lbl_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        lbl_resultado.config(text="Por favor, insira números válidos.")


app = tk.Tk()
app.title("Calculadora Simples")
app.geometry("1000x750")
conteudo = tk.Frame(app)
conteudo.place(relx=0.5, rely=0.5, anchor="center")

entry_numero1 = tk.Entry(conteudo)
entry_numero1.pack(pady=5)
entry_numero2 = tk.Entry(conteudo)
entry_numero2.pack(pady=5)

frame_botoes = tk.Frame(conteudo)
frame_botoes.pack(pady=5)

btn_somar = tk.Button(frame_botoes, text="Somar", command=lambda: calcular("+"))
btn_somar.grid(row=0, column=0, padx=5, pady=5)

btn_subtrair = tk.Button(frame_botoes, text="Subtrair", command=lambda: calcular("-"))
btn_subtrair.grid(row=0, column=1, padx=5, pady=5)

btn_multiplicar = tk.Button(frame_botoes, text="Multiplicar", command=lambda: calcular("*"))
btn_multiplicar.grid(row=1, column=0, padx=5, pady=5)

btn_dividir = tk.Button(frame_botoes, text="Dividir", command=lambda: calcular("/"))
btn_dividir.grid(row=1, column=1, padx=5, pady=5)

lbl_resultado = tk.Label(conteudo, text="Resultado: ")
lbl_resultado.pack(pady=10)

app.mainloop()