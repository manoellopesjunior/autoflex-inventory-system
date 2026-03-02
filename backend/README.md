# 🚀 Autoflex Inventory System - Backend

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-orange)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

API backend desenvolvida como teste prático para a Autoflex.  
O sistema gerencia produtos, matérias-primas e a associação entre eles, permitindo o controle de estoque e preparando a base para cálculos de produção.

---

## 📌 Funcionalidades

- Cadastro de produtos (nome, valor)  
- Cadastro de matérias-primas (quantidade em estoque)  
- Associação de matérias-primas aos produtos com quantidade necessária  
- Atualização e remoção de associações  
- Listagem de produtos e matérias-primas  
- Validação de regras de negócio via API REST  

---

## 🛠 Tecnologias Utilizadas

- **Python 3.11+**  
- **FastAPI** – Framework para APIs REST  
- **SQLAlchemy** – ORM para persistência de dados  
- **Pydantic** – Validação de dados  
- **Uvicorn** – Servidor ASGI  
- **SQLite** (estrutura preparada para PostgreSQL ou MySQL)  

---

## 🗂 Estrutura do Projeto
backend/
├── app/
│ ├── crud/
│ ├── models/
│ ├── routers/
│ ├── schemas/
│ ├── database.py
│ └── main.py
├── requirements.txt
└── README.md

## ▶️ Como Executar

1. Criar e ativar o ambiente virtual:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate

Instalar dependências:

pip install -r requirements.txt

Iniciar o servidor:

python -m uvicorn app.main:app --reload

Acessar a API:

Swagger UI: http://127.0.0.1:8000/docs

OpenAPI JSON: http://127.0.0.1:8000/openapi.json

🔗 Endpoints Principais
Products

POST /products – Criar produto
Exemplo de payload:

{
  "name": "Produto A",
  "price": 49.90
}

GET /products – Listar produtos

PUT /products/{id} – Atualizar produto

{
  "name": "Produto A Atualizado",
  "price": 59.90
}

DELETE /products/{id} – Excluir produto

Raw Materials

POST /raw-materials – Criar matéria-prima

{
  "name": "Matéria-Prima X",
  "quantity": 100
}

GET /raw-materials – Listar matérias-primas

PUT /raw-materials/{id} – Atualizar matéria-prima

DELETE /raw-materials/{id} – Excluir matéria-prima

Product ↔ Raw Material Association

POST /product-raw-materials – Associar matéria-prima a produto

{
  "product_id": 1,
  "raw_material_id": 2,
  "quantity_needed": 5
}

GET /product-raw-materials/product/{product_id} – Listar associações de um produto

DELETE /product-raw-materials/product/{product_id}/raw-material/{raw_material_id} – Remover associação

📐 Requisitos Não Funcionais

Arquitetura baseada em API REST

Separação clara entre backend e frontend

Persistência em banco relacional

Uso de framework para backend

Validação de dados com schemas

Código, variáveis e endpoints em inglês

Preparado para escalabilidade e integração futura com frontend

📝 Registro de Progresso

Estrutura Inicial: projeto criado, ambiente configurado, FastAPI configurado

Arquitetura: separação em routers, models, schemas, CRUD; banco configurado

CRUD Produtos: criação, listagem, atualização e exclusão

CRUD Matérias-Primas: cadastro, listagem, atualização e exclusão

Associação Produto x Matéria-Prima: criação, atualização e exclusão de vínculos

Testes Manuais: validação completa via Swagger UI
