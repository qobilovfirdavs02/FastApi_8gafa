from app.models.departments import Departments
from app.schemas.departments import DepartmentCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_departments(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    departments = db.query(Departments).filter(
        Departments.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(departments), 'departments': departments}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_department(payload: DepartmentCreateUpdateSchema, db: Session = Depends(get_db)):
    new_department = Departments(**payload.dict())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return {"status": "success", "department": new_department}


@router.patch('/{departmentId}')
def update_department(departmentId: int, payload: DepartmentCreateUpdateSchema, db: Session = Depends(get_db)):
    department_query = db.query(Departments).filter(Departments.id == departmentId)
    db_department = department_query.first()

    if not db_department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No department with id: {departmentId} found')
    update_data = payload.dict(exclude_unset=True)
    department_query.filter(Departments.id == departmentId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_department)
    return {"status": "success", "department": db_department}


@router.get('/{departmentId}')
def get_department(departmentId: str, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(Departments.id == departmentId).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No department with id: {id} found")
    return {"status": "success", "department": department}


@router.delete('/{departmentId}')
def delete_department(departmentId: str, db: Session = Depends(get_db)):
    department_query = db.query(Departments).filter(Departments.id == departmentId)
    department = department_query.first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No department with id: {id} found')
    department_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

