from sqlalchemy.orm import Session
from models.model import Category
from schemas.schema import CategoryCreate

def create_category(db: Session, data: CategoryCreate):
    new_cat = Category(**data.model_dump())

    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)

    return new_cat

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_category_by_id(db: Session, cat_id: int):
    return db.query(Category).filter(Category.cat_id == cat_id).first()

def delete_category(db: Session, cat_id: int):
    category = db.query(Category).filter(Category.cat_id == cat_id).first()

    if category is None:
        return None

    db.delete(category)
    db.commit()

    return category