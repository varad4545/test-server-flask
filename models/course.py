from app import db

class Course(db.Model):
    __tablename__='courses'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(40))
    type=db.Column(db.String(40))

    def __init__(self, name, type):
        self.name=name
        self.type=type