import datetime
from unittest.mock import Mock

import pytest

from receipt_tracker.entities import person, receipt, seller
from receipt_tracker.use_cases import list_uc


@pytest.fixture
def receipt_repo():
    receipt1 = receipt.Receipt(
        id=1, date=datetime.datetime(2020, 8, 16),
        seller=1, total=9.67,
        description="Steam game",
        person=1
    )

    receipt2 = receipt.Receipt(
        id=1, date=datetime.datetime(2020, 8, 17),
        seller=2, total=17.86,
        description="Groceries",
        person=1
    )

    receipt3 = receipt.Receipt(
        id=1, date=datetime.datetime(2020, 8, 18),
        seller=3, total=57.36,
        description="Random amazon purchases",
        person=2
    )

    receipt4 = receipt.Receipt(
        id=1, date=datetime.datetime(2020, 8, 19),
        seller=4, total=2.50,
        description="Coin laundry",
        person=2
    )

    return [receipt1, receipt2, receipt3, receipt4]

@pytest.fixture
def person_repo():
    person1 = person.Person(
        id=1, fname='James', lname='Trew'
    )

    person2 = person.Person(
        id=2, fname='Eugene', lname='Min'
    )

    return [person1, person2]

@pytest.fixture
def seller_repo():
    seller1 = seller.Seller(id=1, name='Steam')
    seller2 = seller.Seller(id=2, name='No Frills')
    seller3 = seller.Seller(id=3, name='Amazon')
    seller4 = seller.Seller(id=4, name='Always Clean Coin Laundry')

    return [seller1, seller2, seller3, seller4]


# ---------------------------------- TESTS ---------------------------------- #

def test_list_without_parameters(receipt_repo, person_repo, seller_repo):
    r_repo = Mock()
    r_repo.list.return_value = receipt_repo

    p_repo = Mock()
    p_repo.list.return_value = person_repo

    s_repo = Mock()
    s_repo.list.return_value = seller_repo

    list_ = list_uc.ListUseCase(person_repo, receipt_repo, seller_repo)


