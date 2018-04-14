import pyrebase
config = {
  "apiKey": "AIzaSyCGhlTGJEplQTonGztsdty0QNBNckNC0rE",
  "authDomain": "lahacks2018-bb283.firebaseapp.com",
  "databaseURL": "https://lahacks2018-bb283.firebaseio.com",
  "storageBucket": "",
  "serviceAccount": "/Users/mertdusunceli/Desktop/serviceaccount.json"
}

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
email = "mertdusunceli@gmail.com"
password = "lahacks2018"
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])









