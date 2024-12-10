from app.models.nations import Nations
from app.schemas.nations import ListNationResponse, NationSchema, NationCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_nations(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    nations = db.query(Nations).filter(
        Nations.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(nations), 'nations': nations}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_nation(payload: NationCreateUpdateSchema, db: Session = Depends(get_db)):
    new_nation = Nations(**payload.dict())
    db.add(new_nation)
    db.commit()
    db.refresh(new_nation)
    return {"status": "success", "nation": new_nation}


@router.patch('/{nationId}')
def update_nation(nationId: int, payload: NationCreateUpdateSchema, db: Session = Depends(get_db)):
    nation_query = db.query(Nations).filter(Nations.id == nationId)
    db_nation = nation_query.first()

    if not db_nation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No nation with id: {nationId} found')
    update_data = payload.dict(exclude_unset=True)
    nation_query.filter(Nations.id == nationId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_nation)
    return {"status": "success", "nation": db_nation}


@router.get('/{nationId}')
def get_nation(nationId: str, db: Session = Depends(get_db)):
    nation = db.query(Nations).filter(Nations.id == nationId).first()
    if not nation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No nation with id: {id} found")
    return {"status": "success", "nation": nation}


@router.delete('/{nationId}')
def delete_nation(nationId: str, db: Session = Depends(get_db)):
    nation_query = db.query(Nations).filter(Nations.id == nationId)
    nation = nation_query.first()
    if not nation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No nation with id: {id} found')
    nation_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

