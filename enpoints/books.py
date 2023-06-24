from fastapi import APIRouter, Depends
from firebase.index import db
from middleware.verify_token import verify_token

router = APIRouter()


@router.get("/books/{book_id}")
def get_item(book_id: str, decoded_token=Depends(verify_token)):
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
def get_items(decoded_token=Depends(verify_token)):
    try:
        ref = db.collection("books")
        docs = ref.stream()
        books = []
        for doc in docs:
            books.append(doc.to_dict())
        return {"message": "GET books", "books": books, "code_status": 200}
    except Exception as e:
        return {"message": "GET books", "books": [], "code_status": 404}


@router.get("/read/{user_id}")
def get_items(user_id: str, decoded_token=Depends(verify_token)):
    try:
        user_ref = db.collection("users").document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            user = user_doc.to_dict()
        else:
            return {"message": "GET read books", "books": [], "code_status": 404}

        books = []
        for book in user["readBooks"]:
            ref = db.collection("books").document(book)
            doc = ref.get()
            if doc.exists:
                books.append(doc.to_dict())

        return {"message": "GET read books", "books": books, "code_status": 200}
    except Exception as e:
        return {"message": "GET read books", "books": [], "code_status": 404}

@router.get("/ongoing/{user_id}")
def get_items(user_id: str, decoded_token=Depends(verify_token)):
    try:
        user_ref = db.collection("users").document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            user = user_doc.to_dict()
        else:
            return {"message": "GET on going books", "books": [], "code_status": 404}

        books = []
        for book in user["onGoingBooks"]:
            ref = db.collection("books").document(book)
            doc = ref.get()
            if doc.exists:
                books.append(doc.to_dict())

        return {"message": "GET on going books", "books": books, "code_status": 200}
    except Exception as e:
        return {"message": "GET on going books", "books": [], "code_status": 404}
