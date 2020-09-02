# from receipt_tracker.entities import person, receipt, seller


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
