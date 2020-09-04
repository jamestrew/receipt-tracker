from datetime import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from receipt_tracker.repo.models import Seller, Buyer, Receipt
from receipt_tracker.repo.database import Base


@pytest.fixture(scope='session')
def db_session_empty():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    yield session
    session.close()


@pytest.fixture(scope='function')
def db_data_init():
    return [
        Buyer(name='James Trew'),
        Buyer(name='Eugene Min'),
        Seller(name='Steam'),
        Seller(name='No Frills'),
        Seller(name='Amazon'),
        Seller(name='Always Clean Coin Laundry'),
    ]


@pytest.fixture(scope='function')
def db_data_receipts():
    return [
        Receipt(date=datetime(2020, 8, 16), seller_id=1,
                total=9.67, buyer_id=1, description='Steam game'),
        Receipt(date=datetime(2020, 8, 17), seller_id=2,
                total=17.86, buyer_id=1, description='Groceries'),
        Receipt(date=datetime(2020, 8, 18), seller_id=3,
                total=57.36, buyer_id=2, description='Random amazon purchases'),
        Receipt(date=datetime(2020, 8, 19), seller_id=4,
                total=2.50, buyer_id=2),
    ]


@pytest.fixture(scope='function')
def db_session(db_session_empty, db_data_init, db_data_receipts):
    db_session_empty.add_all(db_data_init)
    db_session_empty.commit()

    db_session_empty.add_all(db_data_receipts)
    db_session_empty.commit()

    yield db_session_empty

    db_session_empty.query(Buyer).delete()
    db_session_empty.query(Seller).delete()
    db_session_empty.query(Receipt).delete()
