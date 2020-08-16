

class Person():
    """docstring for Person"""

    def __init__(self, id, fname, lname):
        super().__init__()
        self.id = id
        self.fname = fname
        self.lname = lname

    @classmethod
    def from_dict(cls, dct):
        return cls(
            id=dct['id'],
            fname=dct['fname'],
            lname=dct['lname']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname
        }