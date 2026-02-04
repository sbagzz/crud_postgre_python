# CRUD com PostgreSQL e Python

Projeto de estudos para praticar operações de CRUD (Create, Read, Update e Delete) utilizando Python e PostgreSQL com a biblioteca `psycopg2`.

<br>

##  Objetivo

Este projeto tem como objetivo consolidar conhecimentos em:

- Conexão com banco de dados PostgreSQL
- Execução de comandos SQL com Python
- Operações de INSERT, SELECT, UPDATE e DELETE
- Boas práticas de segurança com variáveis de ambiente (`.env`)
- Organização básica de um projeto backend

<br>

##  Tecnologias Utilizadas

- **Python**
- **PostgreSQL**
- **psycopg2**
- **python-dotenv**

<br>

##  Estrutura do Projeto

```text
crud_postgre/
├── main.py
├── db.py
├── crud.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

<br>

## Funcionalidades

    Consulta de usuários cadastrados
    Inserção de novos usuários
    Atualização de dados de usuários existentes
    Remoção de usuários do banco de dados
    Menu interativo via terminal


Como rodar o projeto localmente
1. Clonar o repositório
bash

git clone https://github.com
cd crud_postgre

Use o código com cuidado.
2. Criar e ativar o ambiente virtual
bash

python -m venv venv
venv\Scripts\activate

3. Instalar as dependências
bash

pip install -r requirements.txt


4. Configurar as variáveis de ambiente
Crie um arquivo .env baseado no .env.example:
env

DB_NAME=estudos_postgres
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

O arquivo .env não deve ser versionado.
5. Executar o projeto
bash

python main.py

<br>

## Autor
Gabriel Noronha de Araujo
Desenvolvedor Python em formação


