from app.models.students import Students
from app.schemas.students import ListStudentResponse, StudentSchema, StudentCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()


@router.get('/')
def get_students(db:Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    students = db.query(Students).filter(
        Students.middle_name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(students), 'students': students}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreateUpdateSchema, db: Session = Depends(get_db)):
    new_student = Students(**payload.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"status": "success", "student": new_student}


@router.patch('/{studentId}')
def update_student(studentId: int, payload: StudentCreateUpdateSchema, db: Session = Depends(get_db)):
    student_query = db.query(Students).filter(Students.id == studentId)
    db_student = student_query.first()

    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No student with id: {studentId} found')
    update_data = payload.dict(exclude_unset=True)
    student_query.filter(Students.id == studentId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_student)
    return {"status": "success", "student": db_student}



@router.get('/{studentId}')
def get_student(studentId: str, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == studentId).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No student with id: {id} found")
    return {"status": "success", "student": student}


@router.delete('/{studentId}')
def delete_student(studentId: str, db: Session = Depends(get_db)):
    student_query = db.query(Students).filter(Students.id == studentId)
    student = student_query.first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No student with id: {id} found')
    student_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

