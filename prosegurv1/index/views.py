from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials, firestore

cred =  credentials.Certificate(r"C:\Users\Diego\Desktop\prosegurtest-4f39b-firebase-adminsdk-tmqjd-2806cb7b33.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create your views here.

def index(request):
    data =  db.collection("cosas").get()

    data_real = {}

    for a in data:
        data_real["1"] = a.to_dict()

    return render(request,"index.html",data_real)
