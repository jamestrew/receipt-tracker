from receipt_tracker.entities.results import Table


class ListUseCase:
    """Create human-readable list of receipts.

    eg. returns:
        [
            {
                'id': 1,
                'date': '2020/08/16',
                'seller': 'Steam',
                'total': '$9.67',
                'person': 'James Trew',
                'description': 'Steam game'
            },
            ...
        ]

    Args:
        repo (sql repository):  I don't know what I'm doing lol.
    """

    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return self.repo.list()


class GetNames:

    def __init__(self, repo, table):
        self.repo = repo
        self.table = table

    def execute(self):
        return self.repo.list_names(self.table)


def get_entities(repo, table, attr=None):
    if attr is not None and attr not in table.__dict__:
        raise KeyError(f'{table} does not contain the {attr} attribute')
    return repo.list_entities(table, attr)


def create_table(repo, table, fields=[], table_title=None):
    """Instantiates a Table object containing with the following:


    Parameters
    ----------
    repo : SQLRepo
        SQLRepo object with current session.
    table : SQL table model
        Buyer, Seller, or Receipt table model.
    fields : list, optional
        A list of desired fields to be included in the table, by default []
        (all fields).
    table_title : str, optional
        A name to be given to the table, by default None (results to SQL table
        model name).

    Returns
    -------
    Table
        Table object with attr header, rows, title.

    Raises
    ------
    KeyError
        Raised if provided fields are not in table columns.
    """

    header = table.__table__.columns.keys() if not fields else fields

    for field in fields:
        if field not in table.__dict__:
            raise KeyError(f'{table} does not contain the {field} attribute')

    if table_title:
        table_name = table_title
    else:
        table_name = table.__tablename__.capitalize()

    return Table(
        header=header,
        rows=repo.table_rows(fields),
        title=table_name
    )
