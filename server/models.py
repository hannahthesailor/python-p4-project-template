from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Booking(db.Model, SerializerMixin):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    salon = db.Column(db.String, nullable=True)
    stylist = db.Column(db.String, nullable=True)
    appointment = db.Column(db.String, nullable=True)