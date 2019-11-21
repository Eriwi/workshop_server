from server import db


class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    text = db.Column(db.String(500))