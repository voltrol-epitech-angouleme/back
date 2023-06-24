import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from dotenv import load_dotenv

load_dotenv()

data = {
    "type": os.environ.get("TYPE"),
    "project_id": os.environ.get("PROJECT_ID"),
    "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
    "private_key": os.environ.get("PRIVATE_KEY"),
    "client_email": os.environ.get("CLIENT_EMAIL"),
    "client_id": os.environ.get("CLIENT_ID"),
    "auth_uri": os.environ.get("AUTH_URI"),
    "token_uri": os.environ.get("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.environ.get("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.environ.get("CLIENT_X509_CERT_URL"),
    "universe_domain": os.environ.get("UNIVERSE_DOMAIN"),
}

# Get the absolute path of the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Join the directory and file name to get the file's absolute path
file_path = os.path.join(script_directory, 'secret.json')

with open(file_path, "w") as json_file:
    json.dump(data, json_file)

json_file.close()

# Use a service account.
cred = credentials.Certificate(file_path)

print(cred)

firebase_admin.initialize_app(cred)

db = firestore.client()
