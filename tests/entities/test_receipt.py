from receipt_tracker.entities import receipt as r
import datetime


def test_receipt_init():
    receipt = r.Receipt(
        id=1, date=datetime.datetime(2020, 8, 16),
        seller="Steam", total=9.67,
        description="test description",
        person=1
    )

    assert receipt.id == 1
    assert receipt.date == datetime.datetime(2020, 8, 16)
    assert receipt.seller == "Steam"
    assert receipt.total == 9.67
    assert receipt.description == "test description"
    assert receipt.person == 1


def test_receipt_from_dict():
    receipt = r.Receipt.from_dict(
        {
            'id': 1,
            'date': datetime.datetime(2020, 8, 16),
            'seller': "Steam",
            'total': 9.67,
            'description': "test description",
            'person': 1
        }
    )

    assert receipt.id == 1
    assert receipt.date == datetime.datetime(2020, 8, 16)
    assert receipt.seller == "Steam"
    assert receipt.total == 9.67
    assert receipt.description == "test description"
    assert receipt.person == 1


def test_receipt_to_dict():
    receipt_dct = {
        'id': 1,
        'date': datetime.datetime(2020, 8, 16),
        'seller': "Steam",
        'total': 9.67,
        'description': "test description",
        'person': 1
    }

    receipt = r.Receipt.from_dict(receipt_dct)

    assert receipt.to_dict() == receipt_dct
