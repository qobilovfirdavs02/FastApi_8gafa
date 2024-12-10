from app.models.regions import Regions
from app.schemas.regions import RegionCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_regions(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    regions = db.query(Regions).filter(
        Regions.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(regions), 'regions': regions}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_region(payload: RegionCreateUpdateSchema, db: Session = Depends(get_db)):
    new_region = Regions(**payload.dict())
    db.add(new_region)
    db.commit()
    db.refresh(new_region)
    return {"status": "success", "region": new_region}


@router.patch('/{regionId}')
def update_region(regionId: int, payload: RegionCreateUpdateSchema, db: Session = Depends(get_db)):
    region_query = db.query(Regions).filter(Regions.id == regionId)
    db_region = region_query.first()

    if not db_region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No region with id: {regionId} found')
    update_data = payload.dict(exclude_unset=True)
    region_query.filter(Regions.id == regionId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_region)
    return {"status": "success", "region": db_region}


@router.get('/{regionId}')
def get_region(regionId: str, db: Session = Depends(get_db)):
    region = db.query(Regions).filter(Regions.id == regionId).first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No region with id: {id} found")
    return {"status": "success", "region": region}


@router.delete('/{regionId}')
def delete_region(regionId: str, db: Session = Depends(get_db)):
    region_query = db.query(Regions).filter(Regions.id == regionId)
    region = region_query.first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No region with id: {id} found')
    region_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

