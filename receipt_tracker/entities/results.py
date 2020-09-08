
class Result(object):
    """Generic class for holding receipt/seller/person combination data.
        Potentially unnecessary.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def from_dict(cls, dct):
        return cls(**dct)

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()}


class Table:

    def __init__(self, header, rows, title):
        self.header = header
        self.rows = rows
        self.title = title
