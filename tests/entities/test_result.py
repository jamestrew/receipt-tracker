import datetime

from receipt_tracker.entities.results import Result


def test_result_init():
    result = Result(
        id=1, date=datetime.datetime(2020, 8, 16),
        seller=1, total=9.67,
        description="test description",
        person=1
    )

    assert result.id == 1
    assert result.date == datetime.datetime(2020, 8, 16)
    assert result.seller == 1
    assert result.total == 9.67
    assert result.description == "test description"
    assert result.person == 1


def test_result_from_dict():
    result = Result.from_dict(
        {
            'id': 1,
            'date': datetime.datetime(2020, 8, 16),
            'seller': 1,
            'total': 9.67,
            'description': "test description",
            'person': 1
        }
    )

    assert result.id == 1
    assert result.date == datetime.datetime(2020, 8, 16)
    assert result.seller == 1
    assert result.total == 9.67
    assert result.description == "test description"
    assert result.person == 1


def test_result_to_dict():
    result_dct = {
        'id': 1,
        'date': datetime.datetime(2020, 8, 16),
        'seller': 1,
        'total': 9.67,
        'description': "test description",
        'person': 1
    }

    result = Result.from_dict(result_dct)
    assert result.to_dict() == result_dct
