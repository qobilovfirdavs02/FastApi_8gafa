# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root@localhost:3306/db_list2')

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#         

# db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# .env faylidan o'zgaruvchilarni yuklash
load_dotenv()

# .env dagi o'zgaruvchilar
DB_HOST = os.getenv('DB_HOST', 'postgres')  # Docker konteyner ichida 'postgres'
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'studentsapis')  # Bazaning nomi
DB_USER = os.getenv('DB_USER', 'myuser')  # Foydalanuvchi nomi
DB_PASSWORD = os.getenv('DB_PASSWORD', 'myuserpassword')  # Foydalanuvchi paroli

# PostgreSQL uchun DATABASE_URL yaratish
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy engine yaratish
engine = create_engine(DATABASE_URL, echo=True)

# Session yaratish
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Model uchun baza yaratish
Base = declarative_base()

# get_db funksiyasini yaratamiz
def get_db():
    db = SessionLocal()
    try:
        yield db  # Sessionni return qiladi
    finally:
        db.close()  # Ishlatilgandan so'ng yopiladi
