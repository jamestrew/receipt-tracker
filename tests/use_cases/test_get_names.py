from unittest.mock import Mock

import pytest

from receipt_tracker.use_cases import list_uc
from receipt_tracker.repo.models import Buyer


@pytest.fixture
def names_results():
    return ['James Trew', 'Eugene Min', 'Anna Trew']


def test_get_buyer_names(names_results):
    repo = Mock()
    repo.list_names.return_value = names_results

    test_use_case = list_uc.GetNames(repo, Buyer)
    results = test_use_case.execute()

    repo.list_names.assert_called_with(test_use_case.table)
    assert set(results) == set(names_results)
