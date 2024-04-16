from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Salon(db.Model, SerializerMixin):
    __tablename__ = "Salons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    img = db.Column(db.String, nullable=True)
