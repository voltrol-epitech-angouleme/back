import os
import pickle

# Get the absolute path of the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Join the directory and file name to get the file's absolute path
file_path = os.path.join(script_directory, './models/book_recommender_model_book.pkl')

# Load the model
with open(file_path, "rb") as load_file:
    model = pickle.load(load_file)

# Function to get book recommendations based on similarity to a selected book
def get_book_recommendations(user, book_id, num_recommendations, books):
    # Get the selected book's categories
    selected_book = next((book for book in books if book['id'] == book_id), None)
    if selected_book is None:
        print("Invalid book ID.")
        return []

    selected_categories = selected_book['categories']

    # Find similar books based on categories
    similar_books = []
    for book in books:
        if book['id'] != book_id and any(category in book['categories'] for category in selected_categories):
            similar_books.append(book)

    # Sort the similar books by their similarity score (based on the number of matching categories)
    similar_books.sort(key=lambda x: len(set(x['categories']).intersection(selected_categories)), reverse=True)

    # Filter out books already read by the user
    user_read_books = set(user['readBooks'])
    book_recommendations = [book['id'] for book in similar_books if book['id'] not in user_read_books]

    return book_recommendations[:num_recommendations]
