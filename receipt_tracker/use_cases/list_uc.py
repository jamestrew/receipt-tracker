from receipt_tracker.entities import person, receipt, seller

class ListUseCase:

    def __init__(self, person_repo, receipt_repo, seller_repo):
        self.person_repo = person_repo
        self.receipt_repo = receipt_repo
        self.seller_repo = seller_repo


