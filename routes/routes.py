from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.db import sessionLocal
from schemas.schema import CategoryCreate, CategoryResponse
from services.service import create_category, delete_category, get_all_categories, get_category_by_id

router = APIRouter(prefix="/categories", tags=["Categories"])

# DB dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoryResponse)
def add_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, data)

@router.get("/", response_model=List[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)

@router.get("/{cat_id}", response_model=CategoryResponse)
def single_category(cat_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, cat_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category
@router.delete("/{cat_id}")
def remove_category(cat_id: int, db: Session = Depends(get_db)):
    category = delete_category(db, cat_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return {
        "message": "Category deleted successfully",
        "deleted_cat_id": cat_id
    }