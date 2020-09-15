from receipt_tracker.entities.results import Table


def create_table(repo, table, fields=[], table_title=None):

    return Table(
        table=table,
        row_entities=repo.table_rows(table),
        fields=fields,
        title=table_title
    )
