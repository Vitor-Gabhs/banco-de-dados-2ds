import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


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


def visualizar_clientes():
    try:
        with sqlite3.connect("clientes.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, email, telefone FROM clientes")
            registros = cursor.fetchall()
    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro no Banco de Dados",
            f"Não foi possível carregar os clientes: {erro}",
        )
        return

    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Clientes Cadastrados")
    janela_lista.geometry("620x320")

    frame_tabela = tk.Frame(janela_lista, padx=15, pady=15)
    frame_tabela.pack(fill=tk.BOTH, expand=True)

    colunas = ("id", "nome", "email", "telefone")
    tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

    tabela.heading("id", text="ID")
    tabela.heading("nome", text="Nome")
    tabela.heading("email", text="E-mail")
    tabela.heading("telefone", text="Telefone")

    tabela.column("id", width=50, anchor=tk.CENTER)
    tabela.column("nome", width=180, anchor=tk.W)
    tabela.column("email", width=210, anchor=tk.W)
    tabela.column("telefone", width=130, anchor=tk.CENTER)

    scrollbar = ttk.Scrollbar(
        frame_tabela, orient=tk.VERTICAL, command=tabela.yview
    )
    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for cliente in registros:
        tabela.insert("", tk.END, values=cliente)


inicializar_banco()

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.resizable(False, False)

frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack(fill=tk.BOTH, expand=True)
frame_principal.columnconfigure(1, weight=1)

tk.Label(frame_principal, text="Nome:").grid(
    row=0, column=0, sticky="w", padx=(0, 10), pady=5
)
entrada_nome = tk.Entry(frame_principal)
entrada_nome.grid(row=0, column=1, sticky="ew", pady=5)

tk.Label(frame_principal, text="E-mail:").grid(
    row=1, column=0, sticky="w", padx=(0, 10), pady=5
)
entrada_email = tk.Entry(frame_principal)
entrada_email.grid(row=1, column=1, sticky="ew", pady=5)

tk.Label(frame_principal, text="Telefone:").grid(
    row=2, column=0, sticky="w", padx=(0, 10), pady=5
)
entrada_telefone = tk.Entry(frame_principal)
entrada_telefone.grid(row=2, column=1, sticky="ew", pady=5)

frame_botoes = tk.Frame(frame_principal)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=(15, 0))

botao_salvar = tk.Button(
    frame_botoes, text="Salvar", width=12, command=salvar_cliente
)
botao_salvar.pack(side=tk.LEFT, padx=(0, 8))

botao_limpar = tk.Button(
    frame_botoes, text="Limpar", width=12, command=limpar_formulario
)
botao_limpar.pack(side=tk.LEFT, padx=8)

botao_visualizar = tk.Button(
    frame_botoes,
    text="Visualizar Clientes",
    width=16,
    command=visualizar_clientes,
)
botao_visualizar.pack(side=tk.LEFT, padx=(8, 0))

entrada_nome.focus()

janela.mainloop()
