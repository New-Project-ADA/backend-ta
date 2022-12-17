# import pyrebase
import firebase_admin
from firebase_admin import credentials, db

email = 'aannurwahidi17@gmail.com'
password = 'admin123'

firebaseConfig = {
  'apiKey': "AIzaSyDyrTuKjMwArGgzeVqrqFkwN7njOay7AHk",
  'authDomain': "ta-eews.firebaseapp.com",
  'databaseURL': "https://ta-eews-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "ta-eews",
  'storageBucket': "ta-eews.appspot.com",
  'messagingSenderId': "1048300824693",
  'appId': "1:1048300824693:web:83256c6970e9253fbaf03c",
  'measurementId': "G-ZCF5PQ8DC7"
}

path = 'creds/ta-eews-firebase_creds.json'
creds = credentials.Certificate(path)

firebase_admin.initialize_app(creds, {
  'databaseURL': "https://ta-eews-default-rtdb.asia-southeast1.firebasedatabase.app"
})

dbs = db.reference('/mseed_data')

# firebase= pyrebase.initialize_app(firebaseConfig)
# authe = firebase.auth()
# database= firebase.database()
# user = authe.sign_in_with_email_and_password(email, password)