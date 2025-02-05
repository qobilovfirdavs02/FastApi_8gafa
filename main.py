from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.db import engine, Base
from app.routes.nation import router as nationRouter
from app.routes.student import router as studentRouter
from app.routes.region import router as regionRouter
from app.routes.city import router as cityRouter
from app.routes.country import router as countryRouter
from app.routes.department import router as departmentRouter
from app.routes.faculty import router as facultyRouter
from app.routes.group import router as groupRouter


Base.metadata.create_all(bind=engine) 

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cityRouter, tags=['Cities'], prefix='/api/cities')
app.include_router(countryRouter, tags=['Countries'], prefix='/api/countries')
app.include_router(facultyRouter, tags=['Faculties'], prefix='/api/faculties')
app.include_router(departmentRouter, tags=['Departments'], prefix='/api/departments')
app.include_router(groupRouter, tags=['Groups'], prefix='/api/groups')
app.include_router(nationRouter, tags=['Nations'], prefix='/api/nations')
app.include_router(regionRouter, tags=['Regions'], prefix='/api/regions')
app.include_router(studentRouter, tags=['Students'], prefix='/api/students')
app.include_router(departmentRouter, tags=['examens'], prefix='/api/students')



@app.post("/Begin3")
def calculate_perimeter_post(a: float):
    perimeter = 4 * a
    return {"perimeter": perimeter}


@app.get("/Begin1")

def calculate_perimeter(a: float):
    perimeter=4*a
    return {"perimeter": perimeter}


@app.get("/")
def root():
    return {"Salom": "guruhi 403b"}



