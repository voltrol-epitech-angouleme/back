import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Get the absolute path of the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Join the directory and file name to get the file's absolute path
file_path = os.path.join(script_directory, 'secret.json')

# Use a service account.
cred = credentials.Certificate(file_path)

firebase_admin.initialize_app(cred)

db = firestore.client()
