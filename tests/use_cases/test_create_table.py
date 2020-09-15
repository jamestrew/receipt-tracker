from unittest.mock import patch, Mock

from receipt_tracker.use_cases.list_uc import create_table
from receipt_tracker.repo.models import Buyer


@patch('receipt_tracker.use_cases.list_uc.Table')
def test_create_table(mock_Table):
    mock_repo = Mock()
    table_rows = []
    mock_repo.table_rows.return_value = table_rows

    create_table(mock_repo, Buyer)
    mock_Table.assert_called_with(
        table=Buyer,
        row_entities=table_rows,
        fields=[],
        title=None
    )
