

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
