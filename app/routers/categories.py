from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.category import get_category, get_categories, create_category
from app.schemas.category import Category, CategoryCreate
from app.deps import get_db

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_category_route(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)

@router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)
