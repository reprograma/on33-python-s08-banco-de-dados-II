<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Tema da Aula

Turma Online 0n33 | Python | Semana 8 | 2024 | Professora Daviny Letícia

### Instruções

Antes de começar, vamos organizar nosso setup.

* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario]

### Conteúdo Extra

* [Conteúdo Extra: Uso de Funções Agregadas e Joins em SQLite ](./extra/readme.md)


## Introdução ao SQLite

SQLite é um sistema de gerenciamento de banco de dados relacional (SGBD) leve, autocontido e embutido. Ele é amplamente utilizado em aplicativos que requerem um banco de dados eficiente, sem a necessidade de um servidor separado.

#### Instalando e Importando o Módulo `sqlite3`

O módulo `sqlite3` é incluído na biblioteca padrão do Python, então não é necessário instalar pacotes adicionais. Para usá-lo, basta importá-lo no seu script Python:

```python
import sqlite3
```

#### Criando e Conectando ao Banco de Dados

Para conectar a um banco de dados SQLite, usamos a função `sqlite3.connect()`. Se o banco de dados não existir, ele será criado automaticamente.

```python
# Conectando ao banco de dados (ou criando, se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()
```

#### Executando Comandos SQL

A seguir, vamos aprender a executar comandos SQL básicos: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, e `JOIN`.

##### 1. Comando `SELECT`

O comando `SELECT` é usado para buscar dados no banco de dados.

```python
# Selecionando todos os registros de uma tabela
cursor.execute("SELECT * FROM minha_tabela")
resultados = cursor.fetchall()

# Exibindo os resultados
for linha in resultados:
    print(linha)
```

##### 2. Comando `INSERT`

O comando `INSERT` é usado para adicionar novos registros a uma tabela.

```python
# Inserindo um novo registro na tabela
cursor.execute("INSERT INTO minha_tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))

# Salvando (commit) as mudanças
conn.commit()
```

##### 3. Comando `UPDATE`

O comando `UPDATE` é usado para modificar registros existentes.

```python
# Atualizando um registro existente
cursor.execute("UPDATE minha_tabela SET coluna1 = ? WHERE coluna2 = ?", (novo_valor1, valor2))

# Salvando as mudanças
conn.commit()
```

##### 4. Comando `DELETE`

O comando `DELETE` é usado para remover registros de uma tabela.

```python
# Removendo um registro da tabela
cursor.execute("DELETE FROM minha_tabela WHERE coluna1 = ?", (valor1,))

# Salvando as mudanças
conn.commit()
```

#### Usando `JOIN` e `LEFT JOIN`

O comando `JOIN` é utilizado para combinar registros de duas ou mais tabelas com base em uma coluna relacionada.

##### 1. Comando `JOIN`

```python
# Selecionando dados de duas tabelas relacionadas
cursor.execute("""
SELECT a.coluna1, b.coluna2
FROM tabela1 a
JOIN tabela2 b ON a.chave_estrangeira = b.id
""")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
```

##### 2. Comando `LEFT JOIN`

O comando `LEFT JOIN` retorna todos os registros da tabela à esquerda e os registros correspondentes da tabela à direita. Se não houver correspondência, os resultados conterão `NULL`.

```python
# Selecionando dados com LEFT JOIN
cursor.execute("""
SELECT a.coluna1, b.coluna2
FROM tabela1 a
LEFT JOIN tabela2 b ON a.chave_estrangeira = b.id
""")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
```

#### Fechando a Conexão

Após executar todos os comandos necessários, é importante fechar a conexão com o banco de dados.

```python
# Fechando o cursor e a conexão
cursor.close()
conn.close()
```

#### Exemplo Completo

Aqui está um exemplo completo que demonstra a criação de uma tabela, inserção, atualização, seleção, remoção de dados e uso de `JOIN`.

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criando uma tabela
cursor = conn.cursor()

# Inserindo dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Bob", 25))

# Atualizando dados
cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (26, "Bob"))

# Selecionando dados
cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha)

# Removendo dados
cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Alice",))

# Commit das mudanças
conn.commit()

# Fechando a conexão
cursor.close()
conn.close()
```

## Integração de CSV com SQLite usando Python

#### Introdução

Nesta seção, vamos aprender como integrar arquivos CSV com um banco de dados SQLite usando Python. Isso inclui ler dados de um arquivo CSV e inseri-los em um banco de dados SQLite, além de exportar dados do banco de dados para um arquivo CSV.

#### Bibliotecas Necessárias

Para este tutorial, vamos usar as bibliotecas `sqlite3` e `csv`, ambas inclusas na biblioteca padrão do Python. Certifique-se de que você tenha o Python instalado.

#### Instalando e Importando as Bibliotecas

Como `sqlite3` e `csv` são bibliotecas padrão do Python, não é necessário instalar pacotes adicionais. Para usá-las, basta importá-las no seu script Python:

```python
import sqlite3
import csv
```

#### Lendo Dados de um Arquivo CSV e Inserindo no SQLite

Vamos começar lendo dados de um arquivo CSV e inserindo-os em uma tabela do banco de dados SQLite.

##### 1. Criando a Tabela no SQLite

Primeiro, vamos criar uma tabela no banco de dados SQLite onde os dados do CSV serão armazenados. Suponha que temos um arquivo CSV chamado `dados.csv` com as colunas `nome` e `idade`.

```python
import sqlite3

# Conectando ao banco de dados SQLite (ou criando se não existir)
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criando a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Salvando as mudanças
conn.commit()
```

##### 2. Lendo o Arquivo CSV e Inserindo Dados na Tabela

Agora, vamos ler o arquivo CSV e inserir os dados na tabela `usuarios`.

```python
import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Abrindo o arquivo CSV
with open('dados.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Pulando o cabeçalho
    next(leitor_csv)
    
    # Inserindo cada linha do CSV na tabela
    for linha in leitor_csv:
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (linha[0], int(linha[1])))

# Salvando as mudanças
conn.commit()

# Fechando a conexão
cursor.close()
conn.close()
```

#### Exportando Dados do SQLite para um Arquivo CSV

Vamos exportar dados da tabela `usuarios` para um arquivo CSV.

```python
import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Selecionando todos os dados da tabela
cursor.execute("SELECT nome, idade FROM usuarios")
dados = cursor.fetchall()

# Escrevendo os dados para um arquivo CSV
with open('exportados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrevendo o cabeçalho
    escritor_csv.writerow(['nome', 'idade'])
    
    # Escrevendo os dados
    escritor_csv.writerows(dados)

# Fechando a conexão
cursor.close()
conn.close()
```

#### Exemplo Completo

Aqui está um exemplo completo que demonstra como ler dados de um arquivo CSV e inseri-los no SQLite, e como exportar dados do SQLite para um arquivo CSV.

```python
import sqlite3
import csv

# Função para criar a tabela no SQLite
def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    """)
    conn.commit()

# Função para inserir dados do CSV no SQLite
def importar_csv_para_sqlite(arquivo_csv, conn):
    cursor = conn.cursor()
    with open(arquivo_csv, 'r') as csv_file:
        leitor_csv = csv.reader(csv_file)
        next(leitor_csv)  # Pular o cabeçalho
        for linha in leitor_csv:
            cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (linha[0], int(linha[1])))
    conn.commit()

# Função para exportar dados do SQLite para CSV
def exportar_sqlite_para_csv(arquivo_csv, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT nome, idade FROM usuarios")
    dados = cursor.fetchall()
    with open(arquivo_csv, 'w', newline='') as csv_file:
        escritor_csv = csv.writer(csv_file)
        escritor_csv.writerow(['nome', 'idade'])  # Cabeçalho
        escritor_csv.writerows(dados)

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('exemplo.db')

# Criando a tabela
criar_tabela(conn)

# Importando dados do CSV para o SQLite
importar_csv_para_sqlite('dados.csv', conn)

# Exportando dados do SQLite para CSV
exportar_sqlite_para_csv('exportados.csv', conn)

# Fechando a conexão
conn.close()
```

### Normalização de Banco de Dados: Formas Normais (1NF, 2NF, 3NF)

A normalização é um processo que organiza os dados em um banco de dados relacional para reduzir a redundância e melhorar a integridade. As formas normais são regras que um banco de dados pode seguir para garantir uma estrutura organizada.

Primeira Forma Normal (1NF): Garante que cada coluna contenha apenas valores atômicos, e cada célula na tabela contenha um único valor.
Exemplo:

Tabela "Funcionarios":
| ID | Nome        | Habilidades        |
|----|-------------|-------------------|
| 1  | João        | Java, SQL          |
| 2  | Maria       | Python, JavaScript |

Transformação para 1NF:

| ID | Nome  | Habilidade  |
|----|-------|-------------|
| 1  | João  | Java        |
| 1  | João  | SQL         |
| 2  | Maria | Python      |
| 2  | Maria | JavaScript  |


Segunda Forma Normal (2NF): Além de estar na 1NF, cada coluna não chave deve depender totalmente da chave primária.

Terceira Forma Normal (3NF): Além de estar na 2NF, não deve haver dependência transitiva de atributos não chave.


# Funções Agregadas no SQL

As funções agregadas no SQL permitem realizar cálculos em conjuntos de dados, como somar valores, calcular médias, contar registros, e encontrar valores máximos e mínimos. As principais funções agregadas são: `SUM`, `AVG`, `COUNT`, `MAX` e `MIN`. Nesta apostila, vamos aprender sobre cada uma dessas funções com exemplos práticos.

## Criação da Tabela de Exemplo

Vamos começar criando uma tabela chamada `vendas` que usaremos para demonstrar as funções agregadas. A tabela `vendas` possui as seguintes colunas: `id`, `produto`, `quantidade`, `preco_unitario`.

```sql
CREATE TABLE vendas (
    id INT PRIMARY KEY,
    produto VARCHAR(50),
    quantidade INT,
    preco_unitario DECIMAL(10, 2)
);
```

## Inserindo Dados na Tabela

Vamos inserir alguns dados na tabela `vendas` para usar nos exemplos.

```sql
INSERT INTO vendas (id, produto, quantidade, preco_unitario) VALUES
(1, 'Produto A', 10, 20.00),
(2, 'Produto B', 5, 35.00),
(3, 'Produto A', 7, 20.00),
(4, 'Produto C', 3, 50.00),
(5, 'Produto B', 2, 35.00);
```

## Funções Agregadas

### SUM(coluna)

A função `SUM` soma os valores de uma coluna. Por exemplo, para calcular a soma das quantidades de produtos vendidos:

```sql
SELECT SUM(quantidade) AS total_quantidade
FROM vendas;
```

**Resultado:**

| total_quantidade |
|------------------|
| 27               |

### AVG(coluna)

A função `AVG` calcula a média dos valores em uma coluna. Por exemplo, para calcular a média dos preços unitários:

```sql
SELECT AVG(preco_unitario) AS preco_medio
FROM vendas;
```

**Resultado:**

| preco_medio |
|-------------|
| 32.00       |

### COUNT(coluna)

A função `COUNT` conta o número de registros em uma coluna. Por exemplo, para contar o número de registros na tabela `vendas`:

```sql
SELECT COUNT(id) AS total_vendas
FROM vendas;
```

**Resultado:**

| total_vendas |
|--------------|
| 5            |

### MAX(coluna)

A função `MAX` retorna o valor máximo em uma coluna. Por exemplo, para encontrar o preço unitário máximo entre os produtos:

```sql
SELECT MAX(preco_unitario) AS preco_maximo
FROM vendas;
```

**Resultado:**

| preco_maximo |
|--------------|
| 50.00        |

### MIN(coluna)

A função `MIN` retorna o valor mínimo em uma coluna. Por exemplo, para encontrar o preço unitário mínimo entre os produtos:

```sql
SELECT MIN(preco_unitario) AS preco_minimo
FROM vendas;
```

**Resultado:**

| preco_minimo |
|--------------|
| 20.00        |

## Exemplos Combinados

Você também pode combinar essas funções em uma única consulta para obter várias informações de uma só vez:

```sql
SELECT 
    SUM(quantidade) AS total_quantidade,
    AVG(preco_unitario) AS preco_medio,
    COUNT(id) AS total_vendas,
    MAX(preco_unitario) AS preco_maximo,
    MIN(preco_unitario) AS preco_minimo
FROM vendas;
```

**Resultado:**

| total_quantidade | preco_medio | total_vendas | preco_maximo | preco_minimo |
|------------------|-------------|--------------|--------------|--------------|
| 27               | 32.00       | 5            | 50.00        | 20.00        |

---

Com esta apostila, você aprendeu a usar as funções agregadas `SUM`, `AVG`, `COUNT`, `MAX` e `MIN` no SQL, juntamente com exemplos práticos para cada função. Esses exemplos ajudam a entender como realizar cálculos importantes em seus conjuntos de dados.


***
### Exercícios 
* [Exercicio para sala](https://github.com/mflilian/repo-example/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/mflilian/repo-example/tree/main/exercicios/para-casa)

### Material da aula 

### Links Úteis
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)


<p align="center">
Desenvolvido com :purple_heart:  
</p>

