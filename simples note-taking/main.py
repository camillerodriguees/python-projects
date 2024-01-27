import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

# Crie a janela principal
root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")
style = Style(theme='journal')
style = ttk.Style()

# Configure a fonte da aba para ser negrito
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# Crie o bloco de anotações para armazenar as notas
notebook = ttk.Notebook(root, style="TNotebook")

# Carregue as notas salvas
notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

# Crie o bloco de anotações para armazenar as notas
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crie uma função para adicionar uma nova nota
def add_note():
    # Crie uma nova aba para a nota
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="Nova Nota")
    
    # Crie widgets de entrada para o título e conteúdo da nota
    title_label = ttk.Label(note_frame, text="Título:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    
    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)
    
    content_label = ttk.Label(note_frame, text="Conteúdo:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    
    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # Crie uma função para salvar a nota
    def save_note():
        # Obtenha o título e conteúdo da nota
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)
        
        # Adicione a nota ao dicionário de notas
        notes[title] = content.strip()
        
        # Salve o dicionário de notas no arquivo
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        
        # Adicione a nota ao bloco de anotações
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)
        
    # Adicione um botão de salvar ao quadro da nota
    save_button = ttk.Button(note_frame, text="Salvar", 
                             command=save_note, style="secondary.TButton")
    save_button.grid(row=2, column=1, padx=10, pady=10)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            # Adicione a nota ao bloco de anotações
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        # Se o arquivo não existir, não faça nada
        pass

# Chame a função load_notes quando o aplicativo iniciar
load_notes()

# Crie uma função para excluir uma nota
def delete_note():
    # Obtenha o índice da aba atual
    current_tab = notebook.index(notebook.select())
    
    # Obtenha o título da nota a ser excluída
    note_title = notebook.tab(current_tab, "text")
    
    # Mostre uma caixa de diálogo de confirmação
    confirm = messagebox.askyesno("Excluir Nota", 
                                  f"Tem certeza de que deseja excluir {note_title}?")
    
    if confirm:
        # Remova a nota do bloco de anotações
        notebook.forget(current_tab)
        
        # Remova a nota do dicionário de notas
        notes.pop(note_title)
        
        # Salve o dicionário de notas no arquivo
        with open("notes.json", "w") as f:
            json.dump(notes, f)

# Adicione botões à janela principal
new_button = ttk.Button(root, text="Nova Nota", 
                        command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Excluir", 
                           command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()

