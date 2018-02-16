"""music_manager project"""
__author__ = 'Piotr Dyba'

from sqlalchemy import create_engine
from main import db, bcrypt
import models


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()

    user_1 = models.User()
    user_1.username = "piotr"
    user_1.password = bcrypt.generate_password_hash('pppp1234')
    user_1.email = 'piotr@dyba.com.pl'
    user_1.admin = True
    user_1.poweruser = True

    db.session.add(user_1)
    db.session.commit()

    user_2 = models.User()
    user_2.username = "ewelina"
    user_2.password = bcrypt.generate_password_hash('ewelina1')
    user_2.email = 'ewelina@gmail.pl'
    user_2.admin = False
    user_2.poweruser = False

    db.session.add(user_2)
    db.session.commit()

if __name__ == '__main__':
    db_start()