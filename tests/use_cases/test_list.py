from datetime import datetime
from unittest.mock import Mock

import pytest

from receipt_tracker.entities.results import Result
from receipt_tracker.use_cases import list_uc


@pytest.fixture
def receipt_results():
    return [
        Result(
            id=1, date=datetime(2020, 8, 16),
            seller='Steam', total=9.67,
            description="Steam game",
            person='James Trew'
        ),
        Result(
            id=2, date=datetime(2020, 8, 17),
            seller='No Frills', total=17.86,
            description="Groceries",
            person='James Trew'
        ),
        Result(
            id=3, date=datetime(2020, 8, 18),
            seller='Amazon', total=57.36,
            description="Random amazon purchases",
            person='Eugene Min'
        ),
        Result(
            id=4, date=datetime(2020, 8, 19),
            seller='Always Clean Coin Laundry', total=2.50,
            person='Eugene Min'
        ),
    ]


def test_list_without_parameters(receipt_results):
    repo = Mock()
    repo.list.return_value = receipt_results

    test_uc = list_uc.ListUseCase(repo)
    results = test_uc.execute()

    repo.list.assert_called()
    assert results == receipt_results
