## Autoflex Inventory API

Backend API developed as a technical test for Autoflex.

This project is responsible for managing products, raw materials and the
association between them, allowing inventory control and preparation for
production calculations.

## 📌 Description

The system allows:

- Registering products with name and price  
- Registering raw materials with name and stock quantity  
- Associating raw materials to products, including the required quantity of each  
- Managing all data through a REST API  

The project follows an API-first approach, separating back-end and front-end.

## 🛠 Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite (development database)
- Uvicorn


## 📂 Project Structure

autoflex-inventory-system/

    backend/
        app/
            main.py
            routers/
            crud/
            schemas/
            database/

        requirements.txt
        README.md

    docs/
    frontend/

## ⚙️ How to Run the Project

1️⃣ Clone the repository

git clone <repository-url>
cd autoflex-inventory-system/backend

2️⃣ Create and activate virtual environment
python -m venv venv

Windows

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python -m uvicorn app.main:app --reload

## 📑 API Documentation

Swagger UI is available at:

http://127.0.0.1:8000/docs


Through Swagger it is possible to:

Create, list, update and delete products

Create, list, update and delete raw materials

Associate raw materials to products

Remove associations between products and raw materials

## ✅ Implemented Features

- CRUD of Products

- CRUD of Raw Materials

- Association between Products and Raw Materials (many-to-many with quantity)

## 🚧 Current Status

Backend API fully functional

Database persistence implemented

Frontend not implemented

Production calculation feature planned as next step

## 📝 Notes

This project was developed focusing on clarity, organization and separation of
responsibilities (routers, schemas, CRUD and database layers).

Development notes, decisions and challenges will be documented separately.
