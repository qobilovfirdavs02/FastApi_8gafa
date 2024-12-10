from app.models.cities import Cities
from app.schemas.cities import CityCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_cities(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    cities = db.query(Cities).filter(
        Cities.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(cities), 'cities': cities}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_city(payload: CityCreateUpdateSchema, db: Session = Depends(get_db)):
    new_city = Cities(**payload.dict())
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return {"status": "success", "city": new_city}


@router.patch('/{cityId}')
def update_city(cityId: int, payload: CityCreateUpdateSchema, db: Session = Depends(get_db)):
    city_query = db.query(Cities).filter(Cities.id == cityId)
    db_city = city_query.first()

    if not db_city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No city with id: {cityId} found')
    update_data = payload.dict(exclude_unset=True)
    city_query.filter(Cities.id == cityId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_city)
    return {"status": "success", "city": db_city}


@router.get('/{cityId}')
def get_city(cityId: str, db: Session = Depends(get_db)):
    city = db.query(Cities).filter(Cities.id == cityId).first()
    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No city with id: {id} found")
    return {"status": "success", "city": city}


@router.delete('/{cityId}')
def delete_city(cityId: str, db: Session = Depends(get_db)):
    city_query = db.query(Cities).filter(Cities.id == cityId)
    city = city_query.first()
    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No city with id: {id} found')
    city_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

