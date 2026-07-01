-- Banco de Dados - Clientes e Compras
-- Adaptado para SQLite Online

-- Tabela Clientes
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) NOT NULL
);

-- Tabela Compras
CREATE TABLE Compras (
    CompraID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClienteID INTEGER NOT NULL,
    NomeLivro VARCHAR(150) NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

-- Exemplos de INSERT para teste
INSERT INTO Clientes (nomeCliente, emailCliente) VALUES 
('João Silva', 'joao@email.com'),
('Maria Santos', 'maria@email.com'),
('Pedro Oliveira', 'pedro@email.com');

INSERT INTO Compras (ClienteID, NomeLivro) VALUES 
(1, 'Harry Potter e a Pedra Filosofal'),
(1, '1984'),
(2, 'O Senhor dos Anéis'),
(3, 'O Pequeno Príncipe');


SELECT * FROM Clientes;
SELECT * FROM Compras;
