from unittest import mock

import pytest

from receipt_tracker.use_cases.list_uc import create_table
from receipt_tracker.repo.models import Buyer


@pytest.fixture
def repo():
    return mock.Mock()


def test_buyer_basic_table(repo):
    rows = [
        [1, 'James Trew'],
        [2, 'Anna Trew'],
        [3, 'Eugene Min']
    ]
    repo.table_rows.return_value = rows

    test_table = create_table(repo, Buyer)

    assert test_table.header == ['id', 'name']
    assert test_table.rows == rows
    assert test_table.title == 'Buyers'
    repo.table_rows.assert_called_with(Buyer, ['id', 'name'])


def test_buyer_selective_fields_table(repo):
    rows = [
        ['James Trew'],
        ['Anna Trew'],
        ['Eugene Min']
    ]
    repo.table_rows.return_value = rows

    test_table = create_table(repo, Buyer, fields=['name'])

    assert test_table.header == ['name']
    assert test_table.rows == rows
    assert test_table.title == 'Buyers'
    repo.table_rows.assert_called_with(Buyer, ['name'])


def test_buyer_table_invalid_fields(repo):
    with pytest.raises(KeyError):
        create_table(repo, Buyer, fields=['date'])


def test_buyer_different_table_title(repo):
    rows = [
        [1, 'James Trew'],
        [2, 'Anna Trew'],
        [3, 'Eugene Min']
    ]
    repo.table_rows.return_value = rows

    test_table = create_table(repo, Buyer, table_title='Test Table')

    assert test_table.header == ['id', 'name']
    assert test_table.rows == rows
    assert test_table.title == 'Test Table'
    repo.table_rows.assert_called_with(Buyer, ['id', 'name'])
