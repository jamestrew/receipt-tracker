from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine_from_config

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
