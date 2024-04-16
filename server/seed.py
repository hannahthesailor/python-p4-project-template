#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Booking

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        Booking.query.delete()

        print("Starting seed...")

        booking1 = Booking(salon='Gem City Barber', appointment='Beard Trim', stylist='Joe Richardson')
        booking2 = Booking(salon='Gem City Happy Cuts', appointment='Kids Haircut', stylist='Georgie Brown')
        booking3 = Booking(salon='Gem City Updo', appointment='Haircut + Color', stylist='Sara Wilson')

        db.session.add_all([booking1, booking2, booking3])
        db.session.commit()

        # Seed code goes here!
        print("Nice!")
