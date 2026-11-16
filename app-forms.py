import sqlite3
import tkinter as tk
from tkinter import messagebox


def inicializar_banco():
    with sqlite3.connect("clientes.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)
        conexao.commit()


def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()


def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Campos Obrigatórios",
            "Por favor, preencha todos os campos antes de salvar.",
        )
        return

    try:
        with sqlite3.connect("clientes.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone),
            )
            conexao.commit()

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro no Banco de Dados",
            f"Não foi possível salvar os dados: {erro}",
        )


inicializar_banco()

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("360x210")
janela.resizable(False, False)

frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_principal, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
entrada_nome = tk.Entry(frame_principal, width=32)
entrada_nome.grid(row=0, column=1, pady=5)

tk.Label(frame_principal, text="E-mail:").grid(
    row=1, column=0, sticky="w", pady=5
)
entrada_email = tk.Entry(frame_principal, width=32)
entrada_email.grid(row=1, column=1, pady=5)

tk.Label(frame_principal, text="Telefone:").grid(
    row=2, column=0, sticky="w", pady=5
)
entrada_telefone = tk.Entry(frame_principal, width=32)
entrada_telefone.grid(row=2, column=1, pady=5)

frame_botoes = tk.Frame(frame_principal)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=15)

botao_salvar = tk.Button(
    frame_botoes, text="Salvar", width=12, command=salvar_cliente
)
botao_salvar.pack(side=tk.LEFT, padx=10)

botao_limpar = tk.Button(
    frame_botoes, text="Limpar", width=12, command=limpar_formulario
)
botao_limpar.pack(side=tk.LEFT, padx=10)

entrada_nome.focus()

janela.mainloop()
