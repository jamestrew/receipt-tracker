from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from receipt_tracker.repo.database import Base


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
        return f'Receipt({self.id}, {self.date}, {self.total}, {self.description})'


Buyer.purchases = relationship('Receipt',
                               order_by=Receipt.id, back_populates='buyer')
Seller.sales = relationship('Receipt',
                            order_by=Receipt.id, back_populates='seller')
