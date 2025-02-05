# Python image bazasidan foydalanish
FROM python:3.11

# Ishchi papkani yaratish va unga o‘tish
WORKDIR /app

# Rootdagi requirements.txt’ni konteynerga nusxalash
COPY requirements.txt .

# Kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Backend kodlarini konteynerga nusxalash (Agar backend papkasi bo‘lsa)
COPY . .

# FastAPI serverni ishga tushirish
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
