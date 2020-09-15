from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from receipt_tracker.entities.results import EntityRow, ReceiptRow


"""
Variation on the declarative integration of SQLAlchemy with Flask.
See: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/

"""


Base = declarative_base()


class SQLRepo:

    def __init__(self, engine_config):
        self.Base = Base
        self.engine = engine_from_config(engine_config)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        self.Base.query = self.session.query_property()
        from receipt_tracker.repo import models  # noqa

    def init_db(self):
        self.Base.metadata.create_all(self.engine)
        return self.session

    def table_rows(self, table):

        if table.__tablename__ == 'receipts':
            create_row = self._create_receipt_row
        else:
            create_row = self._create_entity_row

        rows = []
        for row in self.session.query(table).all():
            rows.append(create_row(row))
        return rows

    def _create_receipt_row(self, row):
        return ReceiptRow(
            id=row.id,
            date=row.date,
            buyer=row.buyer,
            seller=row.seller,
            total=row.total,
            description=row.description
        )

    def _create_entity_row(self, row):
        return EntityRow(
            id=row.id,
            name=row.name
        )

    # DEPRECATED FUNCTIONS BELOW ###########################################

    def list_entities(self, table, attr=None):
        """Generate a list of SQL model entities or optionally model attributes.
        Used to compile data relevant to a singular table (eg. a list of names in a
        Buyer table).

        Parameters
        ----------
        table : SQL table
            Buyer, Seller or Receipt table.
        attr : str or None, optional
            Column name as a string, by default None

        Returns
        -------
        list
            List of SQL model instances or attributes.

        Example: session = database connection
            >>> session.query(Buyer).all()
            [Buyer(1, James Trew), Buyer(2, Eugene Min)]
            >>> repo.list_names(Buyer)
            [Buyer(1, James Trew), Buyer(2, Eugene Min)]
            >>> self.list_names(Buyer, 'name')
            ['James Trew', 'Eugene Min']
        """

        if attr is None:
            return self.session.query(table).all()
        return [val for (val, ) in self.session.query(getattr(table, attr)).all()]

    def basic_table_rows(self, table, fields):
        """Generate a 2D list of table contents for create_table use case.

        Parameters
        ----------
        table : SQL table model
            Buyer, Seller, or Receipt table.
        fields : list
            A list of table columns, by default all is passed from use case.

        Returns
        -------
        list(list)
            2D list of table contents with desired fields from a SQL table.
        """
        rows = []
        items = [getattr(table, attr) for attr in fields]
        for row in self.session.query(*items).all():
            rows.append([*row])
        return rows
