from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import models
import schemas


def create_category(db: Session, data: schemas.CategoryCreate):
    category = models.Category(**data.model_dump())
    db.add(category)

    try:
        db.commit()
        db.refresh(category)
        return category
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Category name already exists"
        )


def get_categories(db: Session):
    return db.query(models.Category).all()


def create_book(db: Session, data: schemas.BookCreate):
    category = db.query(models.Category).filter(
        models.Category.id == data.category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=400,
            detail="Category does not exist"
        )

    book = models.Book(**data.model_dump())
    db.add(book)

    try:
        db.commit()
        db.refresh(book)
        return book
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="ISBN already exists or book data is invalid"
        )