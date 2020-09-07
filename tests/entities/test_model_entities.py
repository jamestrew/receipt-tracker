import datetime

from receipt_tracker.entities.model_entities import Business, Client, Receipt

# Business Tests ################################################


def test_business_init():
    business = Business(id=1, name='Steam')

    assert business.id == 1
    assert business.name == 'Steam'


def test_business_init_from_dict():
    business = Business.from_dict(
        {
            'id': 1,
            'name': 'Steam'
        }
    )

    assert business.id == 1
    assert business.name == 'Steam'


def test_business_to_dict():
    business_dict = {
        'id': 1,
        'name': 'Steam'
    }

    business = Business.from_dict(business_dict)
    assert business.to_dict() == business_dict


# Client Tests ########################################################
def test_person_init():
    client = Client(id=1, name="James")

    assert client.id == 1
    assert client.name == "James"


def test_person_from_dict():
    client = Client.from_dict(
        {
            'id': 1,
            'name': "James"
        }
    )

    assert client.id == 1
    assert client.name == "James"


def test_client_to_dict():
    client_dict = {
        'id': 1,
        'name': "James"
    }

    client = Client.from_dict(client_dict)
    assert client.to_dict() == client_dict


# Receipt Tests #########################################################
def test_receipt_init():
    receipt = Receipt(
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
    receipt = Receipt.from_dict(
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

    receipt = Receipt.from_dict(receipt_dct)
    assert receipt.to_dict() == receipt_dct


# --------- No Description --------- #


def test_receipt_init_no_descript():
    receipt = Receipt(
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
    receipt = Receipt.from_dict(
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

    receipt = Receipt.from_dict(receipt_dct)
    assert receipt.to_dict() == {'id': 1,
                                 'date': datetime.datetime(2020, 8, 16),
                                 'business': 1,
                                 'total': 9.67,
                                 'description': None,
                                 'client': 1
                                 }
