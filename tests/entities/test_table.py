

import pytest

from receipt_tracker.entities.results import Cell, EntityRow
# from receipt_tracker.repo.models import Buyer


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


# def test_buyer_table_init_defaults(buyer_ents):
#     test_table = Table(Buyer, buyer_ents)

#     assert test_table.table == Buyer
#     assert test_table.fields == ['id', 'name']
#     assert test_table.rows == [
#         [1, 'James Trew'],
#         [2, 'Anna Trew'],
#         [3, 'Jim Halpert']
#     ]
#     assert test_table.title == 'Buyers'
#     assert test_table.header == ['ID', 'Name']


"""
    - invalid fields
    - non-default fields
    - non-default title
    - relationship receipt fields
"""
