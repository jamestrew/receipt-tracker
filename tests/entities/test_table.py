from datetime import date

import pytest

from receipt_tracker.entities.results import Table, Cell, EntityRow, ReceiptRow
from receipt_tracker.repo.models import Buyer, Seller, Receipt


@pytest.fixture
def buyer_ents():
    return [
        EntityRow(
            id=1,
            name='James Trew'
        ),
        EntityRow(
            id=2,
            name='Anna Trew'
        ),
        EntityRow(
            id=3,
            name='Jim Halpert'
        )
    ]


def test_cell_init():
    test_cell = Cell(name='Test Cell', data=2)

    assert test_cell.name == 'Test Cell'
    assert test_cell.data == 2


def test_buyer_table_init_defaults(buyer_ents):
    test_table = Table(Buyer, buyer_ents)

    assert test_table.table == Buyer
    assert test_table.fields == ['id', 'name']
    assert test_table.rows == [
        [1, 'James Trew'],
        [2, 'Anna Trew'],
        [3, 'Jim Halpert']
    ]
    assert test_table.title == 'Buyers'
    assert test_table.headers == ['ID', 'Name']


def test_buyer_table_init_modified(buyer_ents):
    fields = ['name']
    test_table = Table(Buyer, buyer_ents, fields, title='test table')

    assert test_table.table == Buyer
    assert test_table.fields == fields
    assert test_table.rows == [
        ['James Trew'],
        ['Anna Trew'],
        ['Jim Halpert']
    ]
    assert test_table.title == 'test table'
    assert test_table.headers == ['Name']


def test_buyer_table_init_invalid_field(buyer_ents):
    with pytest.raises(KeyError):
        Table(Buyer, buyer_ents, fields=['name', 'date'])


@pytest.fixture
def receipt_ents(db_session):
    return [
        ReceiptRow(
            id=1,
            date=date.fromisoformat('2019-12-04'),
            buyer=db_session.query(Buyer).first(),
            seller=db_session.query(Seller).first(),
            total=50.5,
            description=None
        ), ReceiptRow(
            id=2,
            date=date.fromisoformat('2019-12-05'),
            buyer=db_session.query(Buyer).first(),
            seller=db_session.query(Seller).first(),
            total=2,
            description='Game'
        )
    ]


def test_receipt_table_init_defaults(receipt_ents):
    test_table = Table(Receipt, receipt_ents)

    assert test_table.table == Receipt
    assert test_table.fields == [
        'id', 'date', 'buyer_id', 'buyer_name', 'seller_id',
        'seller_name', 'total', 'description'
    ]
    assert test_table.rows == [
        [1, '2019-12-04', 1, 'James Trew', 1, 'Steam', '50.50', ''],
        [2, '2019-12-05', 1, 'James Trew', 1, 'Steam', '2.00', 'Game']
    ]
    assert test_table.title == 'Receipts'
    assert test_table.headers == [
        'ID', 'Date', 'Buyer ID', 'Buyer Name', 'Seller ID',
        'Seller Name', 'Total', 'Description'
    ]


def test_receipt_table_init_modified(receipt_ents):
    fields = ['date', 'buyer_name', 'seller_name', 'total']
    title = 'Test table'
    test_table = Table(Receipt, receipt_ents, fields, title=title)

    assert test_table.table == Receipt
    assert test_table.fields == fields
    assert test_table.rows == [
        ['2019-12-04', 'James Trew', 'Steam', '50.50'],
        ['2019-12-05', 'James Trew', 'Steam', '2.00']
    ]
    assert test_table.title == title
    assert test_table.headers == ['Date', 'Buyer Name', 'Seller Name', 'Total']


"""
    - invalid fields
    - non-default fields
    - non-default title
    - relationship receipt fields
"""
