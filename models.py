from app import db
from datetime import datetime

class Person(db.Model):
    __tablename__ = 'people'


    pid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)


    def __repr__(self):
        return f'person with name {self.name} and age {self.age}'

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(2048), nullable=False)
    keywords = db.Column(db.String(200), nullable=False)
    rank = db.Column(db.Integer)
    page = db.Column(db.Integer)
    region = db.Column(db.String(10))
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username