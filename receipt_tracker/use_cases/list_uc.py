from receipt_tracker.entities.results import Table


def get_entities(repo, table, attr=None):
    if attr is not None and attr not in table.__dict__:
        raise KeyError(f'{table} does not contain the {attr} attribute')
    return repo.list_entities(table, attr)


def create_table(repo, table, fields=[], table_title=None):

    return Table(
        table=table,
        row_entities=repo.table_rows(table),
        fields=fields,
        title=table_title
    )
