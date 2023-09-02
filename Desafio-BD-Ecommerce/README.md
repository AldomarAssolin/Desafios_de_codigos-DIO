# Projeto de Banco de Dados de E-commerce

## Descrição

Este projeto consiste na criação de um banco de dados relacional para um e-commerce simples. O objetivo é armazenar informações sobre produtos, clientes, pedidos e pagamentos.

### Esquema Lógico

O esquema lógico do banco de dados é baseado no modelo ER conceitual criado no desafio anterior. O diagrama ER e o esquema lógico estão disponíveis no diretório docs do repositório.

### Script SQL

O script SQL para a criação do esquema do banco de dados está disponível no arquivo create_database.sql.

### Dados

O banco de dados foi inicializado com alguns dados de teste. Esses dados estão disponíveis no arquivo data.sql.

### Exemplos de Queries

Aqui estão alguns exemplos de queries criadas para este projeto:

**Recuperar todos os produtos:**

```SQL
SELECT * FROM produto;
```

**Filtrar os produtos por categoria:**

```SQL
SELECT * FROM produto
    WHERE categoria = 'Eletrônicos';
```

**Gerar um atributo derivado do preço:**

```SQL
SELECT produto.nome, produto.preco,
       ROUND(produto.preco * 1.15, 2) AS preco_com_imposto
    FROM produto;
```

**Ordenar os dados por nome:**

```SQL
SELECT * FROM produto
    ORDER BY nome;
```

**Filtrar os produtos por categoria e número de vendas:**

```SQL
SELECT produto.nome, produto.categoria, 
    COUNT(pedido.id) AS numero_de_vendas
    FROM produto
    INNER JOIN pedido ON produto.id = pedido.produto_id
    GROUP BY produto.id
    HAVING produto.categoria = 'Eletrônicos'
    AND COUNT(pedido.id) >= 10;
```

## Conclusão

Este projeto demonstrou a capacidade de criar um banco de dados relacional para um contexto específico. As queries criadas mostram o uso das cláusulas SELECT, WHERE, GROUP BY, HAVING e ORDER BY, entre outras.
