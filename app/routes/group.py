from app.models.groups import Groups
from app.schemas.groups import GroupCreateUpdateSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.config.db import get_db

router = APIRouter()

@router.get('/')
def get_groups(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    groups = db.query(Groups).filter(
        Groups.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(groups), 'groups': groups}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_group(payload: GroupCreateUpdateSchema, db: Session = Depends(get_db)):
    new_group = Groups(**payload.dict())
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return {"status": "success", "group": new_group}


@router.patch('/{groupId}')
def update_group(groupId: int, payload: GroupCreateUpdateSchema, db: Session = Depends(get_db)):
    group_query = db.query(Groups).filter(Groups.id == groupId)
    db_group = group_query.first()

    if not db_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No group with id: {groupId} found')
    update_data = payload.dict(exclude_unset=True)
    group_query.filter(Groups.id == groupId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_group)
    return {"status": "success", "group": db_group}


@router.get('/{groupId}')
def get_group(groupId: str, db: Session = Depends(get_db)):
    group = db.query(Groups).filter(Groups.id == groupId).first()
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No group with id: {id} found")
    return {"status": "success", "group": group}


@router.delete('/{groupId}')
def delete_group(groupId: str, db: Session = Depends(get_db)):
    group_query = db.query(Groups).filter(Groups.id == groupId)
    group = group_query.first()
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No group with id: {id} found')
    group_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

