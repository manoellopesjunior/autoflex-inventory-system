# System Architecture

## Overview

The system follows a client-server architecture using REST APIs.

- Front-end: Web application responsible for user interaction
- Back-end: REST API responsible for business rules and data persistence
- Database: Relational database for storing system data

---

## Architecture Diagram (Conceptual)

Frontend (React)
        |
        | HTTP (JSON)
        v
Backend (FastAPI)
        |
        v
Database (PostgreSQL / MySQL)

---

## Responsibilities

### Front-end
- Display data to the user
- Send requests to the API
- Handle basic form validation
- Consume production suggestion endpoint

### Back-end
- Expose REST endpoints
- Implement business rules
- Calculate production suggestion
- Persist data

### Database
- Store products, raw materials and associations
- Ensure data integrity
