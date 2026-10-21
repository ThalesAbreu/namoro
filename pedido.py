import tkinter as tk
from tkinter import messagebox
import random

def foge(event):
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()

    novo_x = random.randint(50, largura_janela - 100)
    novo_y = random.randint(50, altura_janela - 100)

    botao_nao.place(x=novo_x, y=novo_y)

def aceitou():
    messagebox.showinfo( "Não tinha escolha", "Não Tinha escolha, Obrigado por aceitar o pedido!")

janela = tk.Tk()
janela.title("Pedido Especial")
janela.geometry("400x400")
janela.configure(bg="#ffe5ec")
janela.resizable(False, False)

titulo = tk.Label(janela, text="Você aceita namorar comigo?", font=("Helvetica", 18, "bold"), bg="#030303", fg="#ff477e")
titulo.pack(pady=50)

botao_sim = tk.Button(janela, text="Sim", font=("Helvetica", 14, "bold"), bg="#ff7096", fg="white", command=aceitou, width=8)
botao_sim.place(x=100, y=200)

botao_nao = tk.Button(janela, text="Não", font=("Helvetica", 14, "bold"), bg="#fb6f92", fg="white", width=8)
botao_nao.place(x=250, y=200)

botao_nao.bind("<Enter>", foge)

janela.mainloop()