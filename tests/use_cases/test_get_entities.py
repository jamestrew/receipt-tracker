from unittest.mock import Mock

import pytest

from receipt_tracker.use_cases.list_uc import get_entities
from receipt_tracker.repo.models import Buyer


@pytest.fixture
def repo():
    return Mock()


def test_get_buyers_asserted(repo):
    get_entities(repo, Buyer)

    repo.list_entities.assert_called_with(Buyer, None)


def test_get_buyer_names_asserted(repo):
    get_entities(repo, Buyer, 'name')

    repo.list_entities.assert_called_with(Buyer, 'name')


def test_get_entities_invalid_attr(repo):
    with pytest.raises(KeyError):
        get_entities(repo, Buyer, 'date')
