from app import db

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(40))
    email=db.Column(db.String(40))

    def __init__(self, name, email):
        self.name=name
        self.email=email