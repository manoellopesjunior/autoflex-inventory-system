Autoflex Inventory System

API backend desenvolvida como teste prático para a Autoflex.

Este projeto é responsável por gerenciar produtos, matérias-primas e a associação entre eles, permitindo o controle de estoque e preparando a base para cálculos de produção.

📌 Visão Geral

O sistema permite:

Cadastro de produtos com nome e valor

Cadastro de matérias-primas com quantidade em estoque

Associação de matérias-primas aos produtos, com as quantidades necessárias

Atualização e remoção dessas associações

Listagem de produtos e matérias-primas

Validação de regras de negócio por meio de uma API REST

O projeto foi desenvolvido com foco em boas práticas de backend, arquitetura limpa e validação de dados.

🛠 Tecnologias Utilizadas

Python 3.11+

FastAPI – Framework para APIs REST

SQLAlchemy – ORM para persistência de dados

Pydantic – Validação de dados

Uvicorn – Servidor ASGI

SQLite (estrutura preparada para PostgreSQL ou MySQL)

🗂 Estrutura do Projeto
backend/
├── app/
│   ├── crud/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── database.py
│   └── main.py
├── requirements.txt
└── README.md

▶️ Como Executar o Projeto
1️⃣ Criar e ativar o ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate
2️⃣ Instalar as dependências
pip install -r requirements.txt
3️⃣ Iniciar o servidor
python -m uvicorn app.main:app --reload
4️⃣ Acessar a API

Swagger UI: http://127.0.0.1:8000/docs

OpenAPI JSON: http://127.0.0.1:8000/openapi.json

🔗 Principais Endpoints
Produtos

POST /products

GET /products

PUT /products/{id}

DELETE /products/{id}

Matérias-Primas

POST /raw-materials

GET /raw-materials

PUT /raw-materials/{id}

DELETE /raw-materials/{id}

Associação Produto ↔ Matéria-Prima

POST /product-raw-materials

GET /product-raw-materials/product/{product_id}

DELETE /product-raw-materials/product/{product_id}/raw-material/{raw_material_id}

📐 Requisitos Não Funcionais (RNFs)

Arquitetura baseada em API REST

Separação entre backend e frontend

Persistência de dados em banco relacional

Uso de framework no backend

Validação de dados com schemas

📄 PROGRESS.md — Registro de Progresso do Projeto
Etapas de Desenvolvimento

Etapa 1 – Estrutura Inicial

Criação do projeto

Configuração do ambiente virtual

Estrutura base do FastAPI

Etapa 2 – Definição da Arquitetura

Separação em camadas (routers, models, schemas e CRUD)

Configuração do banco de dados

Etapa 3 – CRUD de Produtos

Criação, listagem e exclusão de produtos

Validação e testes via Swagger

Etapa 4 – CRUD de Matérias-Primas

Cadastro, listagem e exclusão de matérias-primas

Validação de dados de entrada

Etapa 5 – Associação Produto x Matéria-Prima

Criação e atualização do vínculo

Definição de quantidade necessária por produto

Exclusão de associações

Etapa 6 – Testes Manuais

Testes completos via Swagger UI

Validação de todos os endpoints

Etapa 7 – Documentação Final

Criação do README principal

Registro de progresso do projeto

Preparação para entrega e avaliação técnica

Código, variáveis e endpoints em inglês

Estrutura preparada para escalabilidade e integração com frontend

