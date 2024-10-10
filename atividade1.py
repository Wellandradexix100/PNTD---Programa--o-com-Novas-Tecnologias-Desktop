import tkinter as tk
from tkinter import messagebox

#essa é a função que sera executada quando apertar o botão
def mostrar_mensagem():
 messagebox.showinfo("Atenção véio", "Botão Clicado!")
    
#criando a janela
janela = tk.Tk()
janela.title("Janela com botão!")

#definindo o tamanho da janela
janela.geometry("800x500")

#criando o botão
botao= tk.Button(janela, text="clique aqui", command=mostrar_mensagem)

#adiciona o botão a janela
botao.pack(pady=20)

#iniciando o loop da interface
janela.mainloop()
