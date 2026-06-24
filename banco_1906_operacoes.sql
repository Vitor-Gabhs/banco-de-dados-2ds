1. SELECT nome, idade FROM Clientes; 

2. SELECT DISTINCT cidade FROM Clientes; 

3. SELECT DISTINCT cidade FROM Clientes; 

4. SELECT nome FROM Clientes WHERE cidade = 'Curitiba';

5. SELECT nome FROM Clientes WHERE nome LIKE 'C%'; 

6. SELECT nome FROM Clientes WHERE idade BETWEEN 30 AND 40;

7. SELECT nome FROM Clientes WHERE cidade = 'Maringá' AND status = 'Ativo'; 

8. UPDATE Clientes SET idade = idade + 1 WHERE status = 'Ativo';
SELECT * FROM Clientes;

9. UPDATE Clientes SET status = 'Ativo' WHERE nome = 'Carla'; 
SELECT * FROM Clientes;

10. UPDATE Clientes SET idade = idade * 2 WHERE nome = 'Elisa';
SELECT * FROM Clientes;

11. DELETE FROM Clientes WHERE cidade = 'Londrina';
SELECT * FROM Clientes;

12. SELECT nome, cidade FROM Clientes WHERE status = 'Ativo';
