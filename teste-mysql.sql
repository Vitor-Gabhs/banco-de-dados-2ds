_________________SCHEMA_______________________

CREATE TABLE Cliente (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Nome VARCHAR(100) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  Data_Cadastro DATE NOT NULL
  );

INSERT INTO Cliente (Nome, Email, Data_Cadastro)
VALUES ('Ana Silva', 'ana.silva@example.com', '2023-01-15');

INSERT INTO Cliente (Nome, Email, Data_Cadastro)
VALUES ('Carlos Silva', 'carlos.silva@example.com', '2023-02-20'), ('Beatriz Souza', 'beatriz.s@example.com', '2023-03-10');

________________QUERY________________________

SELECT * FROM Cliente;

DROP TABLE Cliente;

SELECT * FROM Cliente;
