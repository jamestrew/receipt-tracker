from datetime import datetime

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


# list_entities #####################################################################
def test_list_buyers(repo):
    test_results = repo.list_entities(Buyer, None)

    assert str(test_results) == '[Buyer(1, James Trew), Buyer(2, Eugene Min), Buyer(3, Anna Trew)]'


def test_list_buyers_name(repo):
    test_results = repo.list_entities(Buyer, 'name')

    assert test_results == ['James Trew', 'Eugene Min', 'Anna Trew']


# basic table_rows ##################################################################
def test_basic_table_rows_all_columns(repo):
    test_table = repo.basic_table_rows(Buyer, ['id', 'name'])

    assert test_table == [
        [1, 'James Trew'],
        [2, 'Eugene Min'],
        [3, 'Anna Trew']
    ]


def test_basic_table_rows_selective(repo):
    test_table = repo.basic_table_rows(Buyer, ['name'])

    assert test_table == [
        ['James Trew'],
        ['Eugene Min'],
        ['Anna Trew']
    ]


# receipt table rows ################################################################
def test_receipt_table_rows_all_columns(repo):
    test_table = repo.receipt_table_rows(['id', 'date', 'seller', 'total',
                                          'buyer', 'description'])

    assert test_table == [
        [1, '2020-08-16', 'James Trew', 'Steam', '9.67', 'Steam game'],
        [2, '2020-08-17', 'James Trew', 'No Frills', '17.86', 'Groceries'],
        [3, '2020-08-18', 'Eugene Min', 'Amazon', '57.36', 'Random amazon purchases'],
        [4, '2020-08-19', 'Eugene Min', 'Always Clean Coin Laundry', '2.50', ''],
    ]


def test_receipt_table_rows_selective(repo):
    test_table = repo.receipt_table_rows(['id', 'seller', 'total', 'description'])

    assert test_table == [
        [1, 'Steam', '9.67', 'Steam game'],
        [2, 'No Frills', '17.86', 'Groceries'],
        [3, 'Amazon', '57.36', 'Random amazon purchases'],
        [4, 'Always Clean Coin Laundry', '2.50', ''],
    ]
