from datetime import date
from dotenv import load_dotenv
from enpoints.books import router as books_router
from enpoints.recommendations import router as recommendations_router
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from firebase.index import db
import os
from pydantic import BaseModel
from recomendations.book import get_book_recommendations
from recomendations.trending import get_books_trending
from recomendations.user import get_book_recommendations_user
from middleware.verify_token import verify_token

load_dotenv()

app = FastAPI()

origins = [
    os.environ.get("ORIGIN"),
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_router)
app.include_router(recommendations_router)


@app.get("/ping")
def ping(decoded_token=Depends(verify_token)):
    return {"message": "pong"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
