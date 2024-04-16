#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Salon

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        Salon.query.delete()

        print("Starting seed...")

        salon1 = Salon(name='Gem City Barber', img="https://thumbs.dreamstime.com/z/barber-shop-22618129.jpg")
        salon2 = Salon(name='Gem City Happy Cuts', img="https://kidsnips.com/wp-content/uploads/2019/07/kidsnips-chicago.jpg")
        salon3 = Salon(name='Gem City Updo', img="https://www.shutterstock.com/image-vector/hair-salon-building-interior-customer-260nw-346105586.jpg")

        db.session.add_all([salon1, salon2, salon3])
        db.session.commit()

        # Seed code goes here!
        print("Nice!")

