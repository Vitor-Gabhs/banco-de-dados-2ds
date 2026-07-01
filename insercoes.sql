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