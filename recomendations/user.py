import os
import pickle
import random

# Get the absolute path of the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Join the directory and file name to get the file's absolute path
file_path = os.path.join(
    script_directory, './models/book_recommender_model_user.pkl')

with open(file_path, "rb") as load_file:
    model = pickle.load(load_file)

# Generate book recommendations for a specific user


def get_book_recommendations_user(user, num_recommendations, books):
    try:
        user_books = [book['id']
                  for book in books if book['id'] in user['readBooks']]


        book_recommendations = []
        for book in books:
            book_id = book['id']
            if book_id not in user_books:
                predicted_rating = model.predict(user["id"], book_id).est
                book_recommendations.append((book_id, predicted_rating))

        # Sort book recommendations by predicted rating
        book_recommendations.sort(key=lambda x: x[1], reverse=True)
        book_recommendations = book_recommendations[:num_recommendations]

        books_res = []
        for book_r in book_recommendations:
            book_id = book_r[0]
            book = next((book for book in books if book['id'] == book_id), None)
            if book is not None:
                books_res.append(book)
        return books_res
        
    except Exception as e:
        book_recommendations = random.sample(books, num_recommendations)
        return book_recommendations

