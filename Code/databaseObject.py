import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter,Or

def dbObj():
    cred = credentials.Certificate("mba-app-25be9-2fb5c2a5685f.json")
    #firebase_admin.initialize_app(cred)
    return firestore.client()