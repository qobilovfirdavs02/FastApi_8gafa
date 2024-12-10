from app.models.countries import Countries
from app.schemas.countries import CountryCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_countries(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    countries = db.query(Countries).filter(
        Countries.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(countries), 'countries': countries}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_country(payload: CountryCreateUpdateSchema, db: Session = Depends(get_db)):
    new_country = Countries(**payload.dict())
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return {"status": "success", "country": new_country}


@router.patch('/{countryId}')
def update_country(countryId: int, payload: CountryCreateUpdateSchema, db: Session = Depends(get_db)):
    country_query = db.query(Countries).filter(Countries.id == countryId)
    db_country = country_query.first()

    if not db_country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No country with id: {countryId} found')
    update_data = payload.dict(exclude_unset=True)
    country_query.filter(Countries.id == countryId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_country)
    return {"status": "success", "country": db_country}


@router.get('/{countryId}')
def get_country(countryId: str, db: Session = Depends(get_db)):
    country = db.query(Countries).filter(Countries.id == countryId).first()
    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No country with id: {id} found")
    return {"status": "success", "country": country}


@router.delete('/{countryId}')
def delete_country(countryId: str, db: Session = Depends(get_db)):
    country_query = db.query(Countries).filter(Countries.id == countryId)
    country = country_query.first()
    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No country with id: {id} found')
    country_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

