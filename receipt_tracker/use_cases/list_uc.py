from receipt_tracker.entities import person, receipt, seller


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

    def __init__(self, person_repo, receipt_repo, seller_repo):
        self.person_repo = person_repo
        self.receipt_repo = receipt_repo
        self.seller_repo = seller_repo

    def execute(self):
        # Requires refactoring
        # In fact I think this whole use case such be handled on the SQL side.

        lst = []
        for receipt in self.receipt_repo:
            for seller in self.seller_repo:
                if seller.id == receipt.seller:
                    seller_name = seller.name
                    break

            for buyer in self.person_repo:
                if buyer.id == receipt.person:
                    buyer_name = f'{buyer.fname} {buyer.lname}'
                    break

            if receipt.description is not None:
                description = receipt.description
            else:
                description = ''

            lst.append(
                {
                    'id': receipt.id,
                    'date': receipt.date.strftime('%Y/%m/%d'),
                    'seller': seller_name,
                    'total': f'${receipt.total:.2f}',
                    'person': buyer_name,
                    'description': description
                }
            )
        return lst
