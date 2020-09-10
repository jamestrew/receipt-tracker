from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from flask_login import UserMixin

from receipt_tracker.repo.sql_repo import Base
from receipt_tracker.flask import login_manager


class Buyer(Base):
    __tablename__ = 'buyers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'Buyer({self.id}, {self.name})'


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'Seller({self.id}, {self.name})'


class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    total = Column(Float, nullable=False)
    buyer_id = Column(Integer, ForeignKey('buyers.id'))
    description = Column(String(140))

    seller = relationship('Seller', back_populates='sales')
    buyer = relationship('Buyer', back_populates='purchases')

    def __repr__(self):
        return f'Receipt({self.id}, {self.buyer.name}, {self.seller.name}, {self.date}, {self.total}, {self.description})'


Buyer.purchases = relationship('Receipt',
                               order_by=Receipt.id, back_populates='buyer')
Seller.sales = relationship('Receipt',
                            order_by=Receipt.id, back_populates='seller')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file})"
