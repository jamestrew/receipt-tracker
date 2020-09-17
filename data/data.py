import json
import random
import datetime

from sqlalchemy.exc import IntegrityError

from receipt_tracker.flask import session
from receipt_tracker.repo.models import Buyer, Receipt, Seller


def generate_buyers(n):
    names = json.loads(open('data/buyers.json').read())
    first = names.get('first')
    last = names.get('last')

    for _ in range(n):
        fullname = random.choice(first) + ' ' + random.choice(last)
        try:
            session.add(Buyer(name=fullname))
        except IntegrityError:
            continue
    session.commit()


def generate_sellers():
    names = json.loads(open('data/sellers.json').read())

    seller_list = [Seller(name=name) for name in names]
    session.add_all(seller_list)
    session.commit()


def generate_receipts(n):
    buyers = session.query(Buyer).all()
    sellers = session.query(Seller).all()

    for _ in range(n):
        buyer = random.choice(buyers)
        seller = random.choice(sellers)
        total = random.randrange(1, 1200) * random.random()
        receipt = Receipt(
            date=_random_date(),
            seller_id=seller.id,
            buyer_id=buyer.id,
            total=total,
            description=f'Stuff from {seller.name} for {total:.2f}'
        )
        try:
            session.add(receipt)
        except IntegrityError:
            continue
    session.commit()


def _random_date():
    now = datetime.datetime.now()
    start = datetime.datetime(2012, 8, 30)

    days_between = (now - start).days
    rand_days = random.randrange(days_between)
    return start + datetime.timedelta(days=rand_days)


def delete_receipts():
    for id in range(4, 404):
        session.query(Receipt).filter(Receipt.id == id).delete(synchronize_session=False)
    session.commit()
