from app.models.faculties import Faculties
from app.schemas.faculties import FacultyCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_faculties(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    faculties = db.query(Faculties).filter(
        Faculties.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(faculties), 'faculties': faculties}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_faculty(payload: FacultyCreateUpdateSchema, db: Session = Depends(get_db)):
    new_faculty = Faculties(**payload.dict())
    db.add(new_faculty)
    db.commit()
    db.refresh(new_faculty)
    return {"status": "success", "faculty": new_faculty}


@router.patch('/{facultyId}')
def update_faculty(facultyId: int, payload: FacultyCreateUpdateSchema, db: Session = Depends(get_db)):
    faculty_query = db.query(Faculties).filter(Faculties.id == facultyId)
    db_facultie = faculty_query.first()

    if not db_facultie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No faculty with id: {facultyId} found')
    update_data = payload.dict(exclude_unset=True)
    faculty_query.filter(Faculties.id == facultyId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_facultie)
    return {"status": "success", "faculty": db_facultie}


@router.get('/{facultyId}')
def get_faculty(facultyId: str, db: Session = Depends(get_db)):
    faculty = db.query(Faculties).filter(Faculties.id == facultyId).first()
    if not faculty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No faculty with id: {id} found")
    return {"status": "success", "faculty": faculty}


@router.delete('/{facultyId}')
def delete_faculty(facultyId: str, db: Session = Depends(get_db)):
    faculty_query = db.query(Faculties).filter(Faculties.id == facultyId)
    faculty = faculty_query.first()
    if not faculty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No faculty with id: {id} found')
    faculty_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

