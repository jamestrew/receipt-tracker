from datetime import date

import pytest

from receipt_tracker.entities.results import ReceiptRow, EntityRow
from receipt_tracker.repo.models import Buyer, Seller


@pytest.fixture
def receiptrow(db_session):
    return ReceiptRow(
        id=1,
        date=date.fromisoformat('2019-12-04'),
        buyer=db_session.query(Buyer).first(),
        seller=db_session.query(Seller).first(),
        total=50.5,
        description=None
    )


@pytest.fixture
def buyerrow():
    return EntityRow(id=1, name='James Trew')


def test_entityrow_init(buyerrow):
    assert buyerrow.id.data == 1
    assert buyerrow.name.data == 'James Trew'


def test_entityrow_init_from_list():
    buyer = EntityRow.from_list([1, 'James Trew'])
    assert buyer.id.data == 1
    assert buyer.name.data == 'James Trew'


def test_entityrow_col_all(buyerrow):
    fields = ['id', 'name']
    assert buyerrow.columns(fields) == ['ID', 'Name']
    assert buyerrow.create_row(fields) == [1, 'James Trew']


def test_entityrow_col_selective(buyerrow):
    fields = ['name']
    assert buyerrow.columns(fields) == ['Name']
    assert buyerrow.create_row(fields) == ['James Trew']


def test_receiptrow_init(receiptrow):

    assert receiptrow.id.data == 1
    assert receiptrow.date.data == '2019-12-04'
    assert receiptrow.buyer_id.data == 1
    assert receiptrow.buyer_name.data == 'James Trew'
    assert receiptrow.seller_id.data == 1
    assert receiptrow.seller_name.data == 'Steam'
    assert receiptrow.total.data == '$50.50'
    assert receiptrow.description.data == ''


def test_receiptrow_col_all(receiptrow):
    fields = [
        'id', 'date', 'buyer_id', 'buyer_name', 'seller_id',
        'seller_name', 'total', 'description'
    ]

    assert receiptrow.columns(fields) == [
        'ID', 'Date', 'Buyer ID', 'Buyer Name', 'Seller ID',
        'Seller Name', 'Total', 'Description'
    ]
    assert receiptrow.create_row(fields) == [
        1, '2019-12-04', 1, 'James Trew', 1, 'Steam', '$50.50', ''
    ]


def test_receiptrow_col_selective(receiptrow):
    fields = [
        'id', 'date', 'buyer_name', 'seller_name', 'total', 'description'
    ]

    assert receiptrow.columns(fields) == [
        'ID', 'Date', 'Buyer Name', 'Seller Name', 'Total', 'Description'
    ]
    assert receiptrow.create_row(fields) == [
        1, '2019-12-04', 'James Trew', 'Steam', '$50.50', ''
    ]
