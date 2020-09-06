from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine_from_config

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

    def init_db(self):
        from receipt_tracker.repo import models  # noqa
        self.Base.metadata.create_all(self.engine)
        return self.session

    def list_names(self, table):
        """Generate a list of names for tables Buyer and Seller

        Parameters
        ----------
        table : SQL table
            Buyer or Seller table with column 'names'.

        Returns
        -------
        [list]
            List of all names in the table.

            eg. table = Buyer
            >>> self.session.query(table).all()
            [Buyer(1, James Trew), Buyer(2, Eugene Min)]
            >>> self.list_names(table)
            [James Trew, Eugene Min]
        """
        return [entity.name for entity in self.session.query(table).all()]
