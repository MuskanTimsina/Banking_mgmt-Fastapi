# Banking Management API

A simple **Banking Management System API** built with **FastAPI**.  
Allows you to **create, read, update, and delete bank accounts**.

---

## Features

- **GET /banks** – Get all bank accounts  
- **GET /banks/{account_id}** – Get a single account by ID  
- **POST /banks** – Create a new bank account  
- **PUT /banks/{account_id}** – Full update of an account  
- **PATCH /banks/{account_id}** – Partial update of an account (optional fields)  
- **DELETE /banks/{account_id}** – Delete an account  

- Handles **ID protection** in PUT and PATCH requests  
- Modular project structure using **routers**  

---


