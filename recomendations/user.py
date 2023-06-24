import os
import pickle

# Get the absolute path of the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Join the directory and file name to get the file's absolute path
file_path = os.path.join(script_directory, './models/book_recommender_model_user.pkl')

with open(file_path, "rb") as load_file:
    model = pickle.load(load_file)

# Generate book recommendations for a specific user

def get_book_recommendations_user(user, num_recommendations, books):
    user_books = [book['id'] for book in books if book['id'] in user['readBooks']]

    book_recommendations = []
    for book in books:
        book_id = book['id']
        if book_id not in user_books:
            predicted_rating = model.predict(user["id"], book_id).est
            book_recommendations.append((book_id, predicted_rating))
    
    
    # Sort book recommendations by predicted rating
    book_recommendations.sort(key=lambda x: x[1], reverse=True)
    return book_recommendations[:num_recommendations]
