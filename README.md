# FastAPI RESTful API with MySQL

This project is a RESTful API built using **FastAPI** and **MySQL** as the database.

---

## 📌 Installation and Setup

Follow these steps to set up and run the project:

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/your-fastapi-project.git
cd your-fastapi-project
```

### 2. **Create a Virtual Environment**
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Set Up the MySQL Database**
Ensure that MySQL is running and create the required database:
```sql
CREATE DATABASE db_list2;
```

### 5. **Configure the Database Connection**
Update your `.env` file or configuration file with the following details:
```
DATABASE_URL = "mysql+pymysql://root@localhost:3306/db_list2"
```

### 6. **Run Database Migrations** (if using SQLAlchemy + Alembic)
```bash
alembic upgrade head
```

### 7. **Run the FastAPI Server**
```bash
uvicorn main:app --reload
```

✅ **API is now running at:** `http://127.0.0.1:8000`

---

## 🚀 API Endpoints

### 📌 **GET /items** - Get a list of items
```bash
GET http://127.0.0.1:8000/items
```

### 📌 **GET /items/{item_id}** - Get a specific item by ID
```bash
GET http://127.0.0.1:8000/items/1
```

### 📌 **POST /items** - Create a new item
```bash
POST http://127.0.0.1:8000/items
Content-Type: application/json
{
    "name": "New Item",
    "description": "Item description",
    "price": 99.99
}
```

### 📌 **PUT /items/{item_id}** - Update an existing item
```bash
PUT http://127.0.0.1:8000/items/1
Content-Type: application/json
{
    "name": "Updated Item",
    "description": "Updated description",
    "price": 89.99
}
```

### 📌 **DELETE /items/{item_id}** - Delete an item
```bash
DELETE http://127.0.0.1:8000/items/1
```

---

## 📜 API Documentation

FastAPI provides automatic API documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 💡 Usage
1. Start the FastAPI server.
2. Open `http://127.0.0.1:8000/docs` to test API endpoints.
3. Use a tool like **Postman** or **cURL** to interact with the API.

---

## ⚡ Troubleshooting
If you encounter issues, check the following:
- Ensure Python, MySQL, and dependencies are installed correctly.
- Verify that the virtual environment is activated.
- Ensure MySQL is running and the database `db_list2` exists.
- Check logs for error messages when running `uvicorn`.

If the issue persists, feel free to open an **Issue** or ask for support.

---

## 📜 License
This project is licensed under the **MIT** license.

---

✅ **Your FastAPI RESTful API with MySQL is now up and running! 🚀**

