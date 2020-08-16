class Receipt():
    """docstring for Receipt"""

    def __init__(self, id, date, seller, total, description, person):
        super().__init__()
        self.id = id  # primary key
        self.date = date
        self.seller = seller
        self.total = total
        self.description = description
        self.person = person  # foreign key

    @classmethod
    def from_dict(cls, dct):
        return cls(
            id=dct['id'],
            date=dct['date'],
            seller=dct['seller'],
            total=dct['total'],
            description=dct['description'],
            person=dct['person']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'seller': self.seller,
            'total': self.total,
            'description': self.description,
            'person': self.person
        }
