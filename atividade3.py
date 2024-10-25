import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_button_click():
    messagebox.showinfo("Informação", "Botão Clicado!")

# Criação da janela principal
root = tk.Tk()
root.title("Interface Gráfica com Imagens")
root.geometry("700x500")

# Carregar a imagem de fundo
bg_image = Image.open("./image/GovPERGB.png")
bg_image = bg_image.resize((600, 150), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Criar um rótulo para a imagem de fundo
bg_label = tk.Label(root, image=bg_photo)
bg_label.pack(pady=30)

# Texto abaixo da imagem de fundo
text_label = tk.Label(root, text="Bem-vindo! Esta é uma interface gráfica com imagens.")
text_label.pack()

# Carregar e redimensionar a imagem do botão
button_image = Image.open("./image/like.png")
button_image = button_image.resize((100, 50), Image.LANCZOS)
button_photo = ImageTk.PhotoImage(button_image)

# Criar um botão com a imagem
button = tk.Button(root, image=button_photo, command=on_button_click)
button.pack(pady=20)

root.mainloop()