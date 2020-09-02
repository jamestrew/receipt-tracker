from receipt_tracker.entities.business import Business


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
