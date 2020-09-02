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
        person_repo (list): List of person objects.
        receipt_repo (list): List of receipt objects.
        seller_repo (list): List of seller objects.
    """

    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return self.repo.list()
