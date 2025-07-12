from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Condominio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    indirizzo = db.Column(db.String(200), nullable=False)

    appartamenti = db.relationship('Appartamento', backref='condominio', cascade='all, delete-orphan')


class Appartamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    proprietario = db.Column(db.String(100), nullable=False)
    condominio_id = db.Column(db.Integer, db.ForeignKey('condominio.id'))
