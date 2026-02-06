# Data Model

This document describes the database structure used by the system.

---

## Table: products

Stores finished products that can be manufactured.

| Field | Type | Description |
|------|------|------------|
| id | integer (PK) | Unique product identifier |
| name | varchar(255) | Product name |
| price | decimal(10,2) | Product unit price |

---

## Table: raw_materials

Stores raw materials used in production.

| Field | Type | Description |
|------|------|------------|
| id | integer (PK) | Unique raw material identifier |
| name | varchar(255) | Raw material name |
| stock_quantity | integer | Available quantity in stock |

---

## Table: product_raw_materials

Associative table defining raw materials required per product.

| Field | Type | Description |
|------|------|------------|
| id | integer (PK) | Unique identifier |
| product_id | integer (FK) | Reference to products.id |
| raw_material_id | integer (FK) | Reference to raw_materials.id |
| required_quantity | integer | Quantity required to produce one unit |

---

## Relationships

- One product → many raw materials
- One raw material → many products
- product_raw_materials represents a many-to-many relationship with extra attributes
