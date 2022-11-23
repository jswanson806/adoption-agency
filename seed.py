"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# remove anything in the database
Pet.query.delete()

# Add sample pets to the db

lucky = Pet(name='Lucky', species='Dog', photo_url='https://images.pexels.com/photos/406014/pexels-photo-406014.jpeg?auto=compress&cs=tinysrgb&w=400', age=3, notes='Loves to chew')
padfoot = Pet(name='Padfoot', species='Dog', photo_url='https://images.pexels.com/photos/4681107/pexels-photo-4681107.jpeg?auto=compress&cs=tinysrgb&w=400', age=2, notes='Super cute')
goliath = Pet(name='Goliath', species='Horse', photo_url='https://images.pexels.com/photos/532310/pexels-photo-532310.jpeg?auto=compress&cs=tinysrgb&w=400', age=7, notes='Looks like a dog', available=False)

db.session.add_all([lucky, padfoot, goliath])

db.session.commit()