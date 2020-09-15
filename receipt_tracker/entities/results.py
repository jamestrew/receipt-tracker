

class Table:

    def __init__(self, table, row_entities, fields=[], title=None):
        """Generate table data.

        Parameters
        ----------
        table : SQLRepo table
            Buyer, Seller, or Receipt table model.
        fields : list
            A list of desired fields to be included in the table.
        row_entities : list(Row)
            A list consisting of Row entities.
        title : str
            A name to be given to the table.
            If None (defaults to SQL table model name capitalized).
        relationship : bool
            Determine whether relationships are shown (ie. buyer name instead of
            buyer id in receipt).

        Raises
        ------
        KeyError
            Raised if provided fields are not in table columns.
        """

        self.table = table
        self.row_type = row_entities[0]

        for field in fields:
            if field not in self.row_type.__dict__.keys():
                raise KeyError(f'Requested field {field} does not exist in \
                               {self.row_type.__class__.__name__}')

        self.fields = fields if fields else list(self.row_type.__dict__.keys())
        self.headers = self.row_type.columns(self.fields)
        self.rows = [row.create_row(self.fields) for row in row_entities]
        self.title = title if title else table.__tablename__.capitalize()


class Cell:

    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data


class Row:

    @ classmethod
    def from_list(cls, lst):
        return cls(*lst)

    def columns(self, fields):
        return [val.name for key, val in self.__dict__.items() if key in fields]

    def create_row(self, fields):
        return [val.data for key, val in self.__dict__.items() if key in fields]


class EntityRow(Row):

    def __init__(self, id, name) -> None:
        self.id = Cell('ID', id)
        self.name = Cell('Name', name)


class ReceiptRow(Row):

    def __init__(self, id, date, buyer, seller, total, description) -> None:
        self.id = Cell('ID', id)
        self.date = Cell('Date', date.strftime('%Y-%m-%d'))
        self.buyer_id = Cell('Buyer ID', buyer.id)
        self.buyer_name = Cell('Buyer Name', buyer.name)
        self.seller_id = Cell('Seller ID', seller.id)
        self.seller_name = Cell('Seller Name', seller.name)
        self.total = Cell('Total', f'{total:.2f}')
        self.description = Cell('Description',
                                '' if description is None else description)
