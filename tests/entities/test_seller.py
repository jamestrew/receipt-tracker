from receipt_tracker.entities.seller import Seller


def test_seller_init():
    seller = Seller(id=1, name='Steam')

    assert seller.id == 1
    assert seller.name == 'Steam'


def test_seller_init_from_dict():
    seller = Seller.from_dict(
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

    seller = Seller.from_dict(seller_dict)
    assert seller.to_dict() == seller_dict
