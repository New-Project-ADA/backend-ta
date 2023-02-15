# import pyrebase
import firebase_admin
from firebase_admin import credentials, db

paths = 'creds/ta-gempa-firebase_creds.json'
creds = credentials.Certificate(paths)

firebase_admin.initialize_app(creds, {
  'databaseURL': "https://ta-gempa-default-rtdb.asia-southeast1.firebasedatabase.app"
})

dbs = db.reference('/mseed_data')

# firebase= pyrebase.initialize_app(firebaseConfig)
# authe = firebase.auth()
# database= firebase.database()
# user = authe.sign_in_with_email_and_password(email, password)