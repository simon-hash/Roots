from database import db

class RootUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.Text, nullable=False)
    Last_Name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)