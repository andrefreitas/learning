from google.appengine.ext import db

class Registration(db.Model):
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    course = db.StringProperty(required=True)
