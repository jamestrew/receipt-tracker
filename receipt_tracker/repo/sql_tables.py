from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    Float,
    ForeignKey
)

Base = declarative_base()


class Buyer(Base):
    __tablename__ = 'buyers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)

    def __repr__(self):
        return f'Buyer({self.id}, {self.first_name}, {self.last_name})'


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

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


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///:memory:', echo=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
