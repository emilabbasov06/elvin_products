from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from ..models import ElektrikModel
from ..database import get_db

router = APIRouter(
  prefix='/api/elektrik',
  tags=['Elektrik']
)


@router.get('/')
def get_products(db: Session = Depends(get_db)):
  products = db.query(ElektrikModel).all()
  if not products:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Found nothing inside the database')
  return products


@router.get('/{id}')
def get_product(id: int, db: Session = Depends(get_db)):
  product = db.query(ElektrikModel).filter(ElektrikModel.id == id).first()
  if not product:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was no product with that specific id: {id}')
  
  return product