DROP DATABASE IF EXISTS VENDINHA;
CREATE DATABASE VENDINHA;
USE VENDINHA;

CREATE TABLE vendas (
    id INT PRIMARY KEY,
    produto VARCHAR(50),
    quantidade INT,
    preco_unitario DECIMAL(10, 2)
);

INSERT INTO vendas (id, produto, quantidade, preco_unitario) VALUES
(1, 'Produto A', 10, 20.00),
(2, 'Produto B', 5, 35.00),
(3, 'Produto A', 7, 20.00),
(4, 'Produto C', 3, 50.00),
(5, 'Produto B', 2, 35.00);

SELECT * FROM  vendas;

SELECT SUM(quantidade) AS total_quantidade FROM vendas;

SELECT AVG(preco_unitario) AS preco_medio FROM vendas;

SELECT COUNT(id) AS total_vendas FROM vendas;

SELECT MAX(preco_unitario) AS preco_maximo FROM vendas;

SELECT MIN(preco_unitario) AS preco_minimo FROM vendas;

SELECT
    SUM(quantidade) AS total_quantidade,
    AVG(preco_unitario) AS preco_medio,
    COUNT(id) AS total_vendas,
    MAX(preco_unitario) AS preco_maximo,
    MIN(preco_unitario) AS preco_minimo
FROM vendas;