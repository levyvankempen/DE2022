from app import db


class Wordcount(db.Model):
    word = db.Column('word', db.String, primary_key=True)
    count = db.Column('count', db.Integer)