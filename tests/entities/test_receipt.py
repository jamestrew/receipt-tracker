from receipt_tracker.entities import receipt as r
import datetime


def test_receipt_init():
    receipt = r.Receipt(
        id=1, date=datetime.datetime(2020, 8, 16),
        business=1, total=9.67,
        description="test description",
        client=1
    )

    assert receipt.id == 1
    assert receipt.date == datetime.datetime(2020, 8, 16)
    assert receipt.business == 1
    assert receipt.total == 9.67
    assert receipt.description == "test description"
    assert receipt.client == 1


def test_receipt_from_dict():
    receipt = r.Receipt.from_dict(
        {
            'id': 1,
            'date': datetime.datetime(2020, 8, 16),
            'business': 1,
            'total': 9.67,
            'description': "test description",
            'client': 1
        }
    )

    assert receipt.id == 1
    assert receipt.date == datetime.datetime(2020, 8, 16)
    assert receipt.business == 1
    assert receipt.total == 9.67
    assert receipt.description == "test description"
    assert receipt.client == 1


def test_receipt_to_dict():
    receipt_dct = {
        'id': 1,
        'date': datetime.datetime(2020, 8, 16),
        'business': 1,
        'total': 9.67,
        'description': "test description",
        'client': 1
    }

    receipt = r.Receipt.from_dict(receipt_dct)
    assert receipt.to_dict() == receipt_dct


# --------- No Description --------- #


def test_receipt_init_no_descript():
    receipt = r.Receipt(
        id=1, date=datetime.datetime(2020, 8, 16),
        business=1, total=9.67,
        client=1
    )

    assert receipt.id == 1
    assert receipt.date == datetime.datetime(2020, 8, 16)
    assert receipt.business == 1
    assert receipt.total == 9.67
    assert receipt.description is None
    assert receipt.client == 1


def test_receipt_from_dict_no_descript():
    receipt = r.Receipt.from_dict(
        {
            'id': 1,
            'date': datetime.datetime(2020, 8, 16),
            'business': 1,
            'total': 9.67,
            'client': 1
        }
    )

    assert receipt.id == 1
    assert receipt.date == datetime.datetime(2020, 8, 16)
    assert receipt.business == 1
    assert receipt.total == 9.67
    assert receipt.description is None
    assert receipt.client == 1


def test_receipt_to_dict_no_descript():
    receipt_dct = {
        'id': 1,
        'date': datetime.datetime(2020, 8, 16),
        'business': 1,
        'total': 9.67,
        'client': 1
    }

    receipt = r.Receipt.from_dict(receipt_dct)
    assert receipt.to_dict() == {'id': 1,
                                 'date': datetime.datetime(2020, 8, 16),
                                 'business': 1,
                                 'total': 9.67,
                                 'description': None,
                                 'client': 1
                                 }
