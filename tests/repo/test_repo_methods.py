import pytest

from receipt_tracker.repo.models import Buyer, Receipt
from receipt_tracker.entities.results import EntityRow, ReceiptRow
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


# basic table_rows #####################################################
def test_basic_table_rows(repo):
    test_table = repo.table_rows(Buyer)

    assert len(test_table) == 3
    assert isinstance(test_table[0], EntityRow) is True
    assert test_table[0].id.data == 1
    assert test_table[0].name.data == 'James Trew'
    assert isinstance(test_table[0], EntityRow) is True
    assert test_table[1].id.data == 2
    assert test_table[1].name.data == 'Eugene Min'
    assert isinstance(test_table[0], EntityRow) is True
    assert test_table[2].id.data == 3
    assert test_table[2].name.data == 'Anna Trew'


# receipt table rows ###################################################
def test_receipt_table_rows(repo):
    test_table = repo.table_rows(Receipt)

    assert len(test_table) == 4
    assert isinstance(test_table[0], ReceiptRow) is True
    assert test_table[0].id.data == 1
    assert test_table[0].date.data == '2020-08-16'
    assert test_table[0].buyer_id.data == 1
    assert test_table[0].buyer_name.data == 'James Trew'
    assert test_table[0].seller_id.data == 1
    assert test_table[0].seller_name.data == 'Steam'
    assert test_table[0].total.data == '9.67'
    assert test_table[0].description.data == 'Steam game'
