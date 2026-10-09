from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models
import schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Book Inventory API",
    description="REST API for managing library books and categories",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Library Book Inventory API is running"}


@app.post(
    "/categories/",
    response_model=schemas.CategoryResponse,
    status_code=201
)
def add_category(
    data: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_category(db, data)


@app.get(
    "/categories/",
    response_model=list[schemas.CategoryResponse]
)
def list_categories(
    db: Session = Depends(get_db)
):
    return crud.get_categories(db)


@app.post(
    "/books/",
    response_model=schemas.BookResponse,
    status_code=201
)
def add_book(
    data: schemas.BookCreate,
    db: Session = Depends(get_db)
):
    return crud.create_book(db, data)


@app.get(
    "/books/",
    response_model=list[schemas.BookResponse]
)
def list_books(
    category_id: int | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_books(db, category_id)


@app.get(
    "/books/{book_id}",
    response_model=schemas.BookResponse
)
def book_details(
    book_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_book(db, book_id)


@app.put(
    "/books/{book_id}",
    response_model=schemas.BookResponse
)
def edit_book(
    book_id: int,
    data: schemas.BookUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_book(db, book_id, data)


@app.delete("/books/{book_id}")
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_book(db, book_id)