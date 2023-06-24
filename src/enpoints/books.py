from fastapi import APIRouter
from firebase.index import db

router = APIRouter()

@router.get("/books/{book_id}")
def get_item(book_id: str):
    try:
        ref = db.collection("books").document(book_id)
        doc = ref.get()
        if doc.exists:
            return {"message": "GET book", "book": doc.to_dict(), "code_status": 200}
        else:
            return {"message": "GET book", "book": {}, "code_status": 404}
    except Exception as e:
        return {"message": "GET book", "books": {}, "code_status": 404}


@router.get("/books")
def get_items():
    try:
        ref = db.collection("books")
        docs = ref.stream()
        books = []
        for doc in docs:
            books.append(doc.to_dict())
        return {"message": "GET books", "books": books, "code_status": 200}
    except Exception as e:
        return {"message": "GET books", "books": [], "code_status": 404}