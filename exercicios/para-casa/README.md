# Exercício de Casa 🏠 

### Integração Completa de CSV com SQLite usando Python

#### Objetivo

A ideia aqui é praticar como integrar arquivos CSV com um banco de dados SQLite usando Python. Vamos criar um banco de dados, importar dados de um arquivo CSV para uma tabela, fazer operações de CRUD (Create, Read, Update, Delete) e, no final, exportar os dados da tabela para um novo arquivo CSV.

#### Descrição do Exercício

1. **Criando o Banco de Dados e a Tabela**
   - Crie um banco de dados SQLite chamado `livraria.db`.
   - Crie uma tabela chamada `livros` com as seguintes colunas:
     - `id` (INTEGER, chave primária, autoincremento)
     - `titulo` (TEXT)
     - `autor` (TEXT)
     - `ano` (INTEGER)
     - `preco` (REAL)

2. **Importando Dados de um CSV**
   - Crie um arquivo CSV chamado `livros.csv` com as colunas `titulo`, `autor`, `ano`, e `preco`.
   - Adicione pelo menos 5 registros no arquivo `livros.csv`.
   - Escreva um script Python que leia os dados do `livros.csv` e insira-os na tabela `livros`.

3. **Consultando e Exibindo Dados**
   - Escreva um script Python que selecione e exiba todos os registros da tabela `livros`.

4. **Atualizando Dados**
   - Escreva um script Python que atualize o preço de um livro específico (por exemplo, mude o preço do livro com `id` 1 para 29.99).

5. **Removendo Dados**
   - Escreva um script Python que remova um livro específico da tabela (por exemplo, remova o livro com `id` 3).

6. **Exportando Dados para CSV**
   - Escreva um script Python que exporte os dados da tabela `livros` para um novo arquivo CSV chamado `exportados_livros.csv`.

### Exemplo do arquivo livros.csv

Crie um arquivo CSV chamado `livros.csv` com o seguinte conteúdo:

```csv
titulo,autor,ano,preco
Livro A,Autor A,2020,25.99
Livro B,Autor B,2019,19.99
Livro C,Autor C,2018,29.99
Livro D,Autor D,2021,15.99
Livro E,Autor E,2022,22.99
```

#### Tarefas Extras

Para dar um up nas suas habilidades, você pode adicionar as seguintes funcionalidades aos seus scripts:

1. **Validação de Dados**:
   - Adicione validações para garantir que os dados lidos do CSV sejam válidos antes de inseri-los no banco de dados.

2. **Tratamento de Erros**:
   - Adicione tratamento de exceções para lidar com possíveis erros durante a leitura, inserção e atualização de dados.

3. **Interatividade**:
   - Torne seus scripts interativos, solicitando entradas do usuário para operações como inserção, atualização e remoção de dados.

#### Envio do Exercício

Depois de terminar o exercício, você deve ter os seguintes arquivos:

- `criar_banco.py`
- `importar_csv.py`
- `consultar_livros.py`
- `atualizar_livro.py`
- `remover_livro.py`
- `exportar_csv.py`
- `livros.csv`

Teste todos os scripts para garantir que estão funcionando certinho antes de enviar.

Boa sorte!
---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).