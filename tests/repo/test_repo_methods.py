import pytest


from receipt_tracker.repo.models import Buyer
from receipt_tracker.repo.sql_repo import SQLRepo


@pytest.fixture(scope='function')
def repo(db_data_init, db_data_receipts):
    CONFIG = {'sqlalchemy.url': 'sqlite:///:memory:'}
    repo = SQLRepo(CONFIG)
    session = repo.init_db()

    session.add_all(db_data_init)
    session.add_all(db_data_receipts)
    session.commit()

    yield repo
    session.remove()


def test_list_buyers(repo):
    test_results = repo.list_entities(Buyer, None)

    assert str(test_results) == '[Buyer(1, James Trew), Buyer(2, Eugene Min), Buyer(3, Anna Trew)]'


def test_list_buyers_name(repo):
    test_results = repo.list_entities(Buyer, 'name')

    assert test_results == ['James Trew', 'Eugene Min', 'Anna Trew']
