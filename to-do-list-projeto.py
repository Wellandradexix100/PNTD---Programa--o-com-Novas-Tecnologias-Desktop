# Importação da biblioteca
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Funções para dar logica aos botões
# Função adicionar tarefa
def adicionar_tarefa():
 if tarefa := entrada_tarefa.get():
  tarefa_lista.insert(tk.END, tarefa)
  entrada_tarefa.delete(0, tk.END)
 else:
  messagebox.showwarning(title='Atenção!', message="Digite uma tarefa para ser adicionada!")

# Função remover tarefa
def remover_tarefa():
 if tarefa_selecionada := tarefa_lista.curselection():
  tarefa_lista.delete(tarefa_selecionada)
 else:
  messagebox.showwarning(title='Atenção!', message="Selecione a tarefa para remover!")

# Função de marcar a tarefa como concluida
def marcar_concluida():
 if tarefa_selecionada := tarefa_lista.curselection():
  tarefa = tarefa_lista.get(tarefa_selecionada)
  tarefa_lista.delete(tarefa_selecionada)
  tarefa_lista.insert(tarefa_selecionada, f"👌{tarefa}")
 else:
  messagebox.showwarning(title='Atenção!', message="Selecione a tarefa para marcar como concluida")

# Função para configurar a imagem de fundo
def definir_fundo(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((900, 600)) 
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_fundo = tk.Label(janela, image=imagem_tk)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1) 
    label_fundo.image = imagem_tk 

# Iniciando a janela e definindo seus parametros
janela = tk.Tk()
janela.configure(background='grey')
janela.title("Gerenciador de Tarefas")
janela.geometry("900x600")

# Define a imagem de fundo 
caminho_da_imagem = "./image/fundo.jpg"
definir_fundo(caminho_da_imagem)
p = tk.Label(text = "GERENCIADOR DE TAREFAS SIMPLES", background='grey', font='roboto')
p.pack(pady=10)

# Campo de texto para entrada de dados
entrada_tarefa = tk.Entry(janela, width=50, border='4', font='arial')
entrada_tarefa.pack(pady=10)

# Espaço para os botões e seus parametros
# Botão adicionar tarefa
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa, background= 'yellow')
botao_adicionar.pack(pady=5)
# Botão de remover tarefa
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa, background='red')
botao_remover.pack(pady=5)
#botão de tarefa concuilda
botao_concluir = tk.Button(janela, text="Marcar como Concluída", command=marcar_concluida, background='green')
botao_concluir.pack(pady=5)

# Espaço para observação das tarefas e seus parametros visuais
tarefa_lista = tk.Listbox(janela, width=50, font='roboto', border='2')
tarefa_lista.pack(pady=10)

# Loop da janela tkinter
janela.mainloop()
