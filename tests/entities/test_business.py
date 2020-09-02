from receipt_tracker.entities.business import Business


def test_seller_init():
    seller = Business(id=1, name='Steam')

    assert seller.id == 1
    assert seller.name == 'Steam'


def test_seller_init_from_dict():
    seller = Business.from_dict(
        {
            'id': 1,
            'name': 'Steam'
        }
    )

    assert seller.id == 1
    assert seller.name == 'Steam'


def test_seller_to_dict():
    seller_dict = {
        'id': 1,
        'name': 'Steam'
    }

    seller = Business.from_dict(seller_dict)
    assert seller.to_dict() == seller_dict
