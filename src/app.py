from datetime import date
from dotenv import load_dotenv
from enpoints.books import router as books_router
from enpoints.recommendations import router as recommendations_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from firebase.index import db
import os
from pydantic import BaseModel
from recomendations.book import get_book_recommendations
from recomendations.trending import get_books_trending
from recomendations.user import get_book_recommendations_user
from firebase_admin import auth
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

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
