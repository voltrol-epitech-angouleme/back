from fastapi import APIRouter
from firebase.index import db
from recomendations.trending import get_books_trending
from recomendations.user import get_book_recommendations_user
from recomendations.book import get_book_recommendations
from pydantic import BaseModel
from middleware.verify_token import verify_token

router = APIRouter()

@router.get("/trending")
def get_trending_books(decoded_token=Depends(verify_token)):
    try:
        return get_books_trending(30)
    except Exception as e:
        return {"message": "GET trending books", "books": [], "code_status": 404}

@router.get("/recommendation")
def books_user_recommendations(user_id: str, decoded_token=Depends(verify_token)):
    try:
        book_ref = db.collection("books")
        book_docs = book_ref.stream()
        books = []
        for doc in book_docs:
            books.append(doc.to_dict())

        user_ref = db.collection("users").document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            user = user_doc.to_dict()
            return {"message": "GET user recommendations", "books": get_book_recommendations_user(user, 30, books), "code_status": 200}
        else:
            return {"message": "GET user recommendations", "books": [], "code_status": 404}
    except Exception as e:
        return {"message": "GET user recommendations", "books": [], "code_status": 404}

class Filters(BaseModel):
    book_id: str
    user_id: str

@router.post("/recommendation/book")
def books_book_recommendations(filters: Filters):
    book_id = filters.book_id
    user_id = filters.user_id

    user_ref = db.collection("users").document(user_id)
    user_doc = user_ref.get()
    if user_doc.exists:
        user = user_doc.to_dict()
    else:
        return {"message": "GET user recommendations", "books": [], "code_status": 404}

    book_ref = db.collection("books")
    book_docs = book_ref.stream()
    books = []
    for doc in book_docs:
        books.append(doc.to_dict())
    return {"message": "GET book recommendations", "books": get_book_recommendations(user, book_id, 30, books), "code_status": 200}