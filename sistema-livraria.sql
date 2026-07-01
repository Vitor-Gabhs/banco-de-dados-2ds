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


-- Inserção de dados na tabela Clientes
INSERT INTO Clientes (nomeCliente, emailCliente) VALUES 
('Carlos Silva', 'carlos@email.com'),
('Ana Souza', 'ana@email.com'),
('Mariana Costa', 'mariana@email.com'),
('Bruno Santos', 'bruno@email.com'),
('Fernanda Oliveira', 'fernanda@email.com');

-- Inserção de dados na tabela Compras
INSERT INTO Compras (ClienteID, NomeLivro) VALUES 
(1, 'Harry Potter e a Pedra Filosofal'),
(1, '1984'),
(2, 'O Senhor dos Anéis'),
(2, 'O Código da Vinci'),
(3, 'O Pequeno Príncipe'),
(3, 'Cem Anos de Solidão'),
(4, 'A Revolução dos Bichos'),
(5, 'O Grande Gatsby');

-- Visualizar dados das tabelas
SELECT * FROM Clientes;
SELECT * FROM Compras;

-- Consulta com INNER JOIN
-- Retorna o nome do cliente e o nome do livro para todas as compras realizadas

SELECT 
    c.nomeCliente,
    cp.NomeLivro
FROM Clientes c
INNER JOIN Compras cp ON c.ID = cp.ClienteID
ORDER BY c.nomeCliente, cp.NomeLivro;
