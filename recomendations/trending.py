import random
from datetime import datetime
from firebase.index import db


try:
    ref = db.collection("books")
    docs = ref.stream()
    books = []
    for doc in docs:
        books.append(doc.to_dict())
    # Get the top 30 trending books
except Exception as e:
    books = []



# Define a function to calculate the trending score for a book
def calculate_trending_score(book):
    # Adjust weights according to your preference
    is_read_weight = 0.4
    rating_weight = 0.3
    update_date_weight = 0.2
    create_date_weight = 0.1

    # Calculate the trending score
    is_read_score = len(book["isReadBy"]) * is_read_weight


    if book["ratings"]:
        rating_score = sum([rating["rating"] for rating in book["ratings"]]) / len(book["ratings"]) * rating_weight
    else:
        rating_score = 0

    update_date_score = (datetime.now() - datetime.fromisoformat(book["updatedAt"])).days * update_date_weight
    create_date_score = (datetime.now() - datetime.fromisoformat(book["createdAt"])).days * create_date_weight

    trending_score = is_read_score + rating_score - update_date_score + create_date_score
    return trending_score

# Sort the books based on trending score in descending order

def get_books_trending(num_books):
    sorted_books = sorted(books, key=calculate_trending_score, reverse=True)
    return {"message": "GET books", "books": sorted_books[:num_books], "code_status": 200}
   

