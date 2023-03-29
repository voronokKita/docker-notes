from datetime import datetime, timezone

from sqlalchemy import (
    create_engine, Column, String, Text,
    Integer, DateTime, Boolean, Sequence,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Query


def current_time():
    return datetime.now(timezone.utc).replace(microsecond=0)


# Models
ModelBase = declarative_base()


class TestTable(ModelBase):
    __tablename__ = 'test'
    id = Column('id', Integer, primary_key=True)
    num = Column('num', Integer)
    txt = Column('txt', String(10))


class Note(ModelBase):
    __tablename__ = 'notes'
    id = Column('id', Integer, primary_key=True)
    data = Column('data', DateTime(timezone=True), nullable=False, default=current_time)
    txt = Column('txt', Text, nullable=False)


# Transactions
url = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(
    user='megauser',
    password='foobarbaz',
    host='postgres',
    port='5432',
    dbname='notes_project_data'
)
DB_ENGINE = create_engine(url, future=True)
DB_SESSION = sessionmaker(bind=DB_ENGINE)


class TestTransactions:
    # @classmethod
    # def set_up():
    #     TestTable.metadata.create_all(DB_ENGINE)

    # @classmethod
    # def tear_down():
    #     TestTable.metadata.drop_all(DB_ENGINE)

    def write_test(self, num, txt) -> True:
        with DB_SESSION.begin() as session:
            row = TestTable(num=num, txt=txt)
            session.add(row)
        return True

    def read_test(self, row: int = None) -> Query | list[Query] | None:
        with DB_SESSION() as session:
            if not row or row == 0:
                return session.query(TestTable).filter().all()
            else:
                return session.query(TestTable).filter_by(id=row).first()


class NoteTransactions:
    # @classmethod
    # def set_up():
    #     Note.metadata.create_all(DB_ENGINE)

    # @classmethod
    # def tear_down():
    #     Note.metadata.drop_all(DB_ENGINE)

    def read_note(self, id_: int) -> Query | None:
        with DB_SESSION() as session:
            return session.query(Note).filter_by(id=id_).first()

    def read_note_list(self) -> list[Query] | None:
        with DB_SESSION() as session:
            return session.query(Note).filter().all()

    def write_note(self, s: str) -> True:
        with DB_SESSION.begin() as session:
            session.add(Note(txt=s))
        return True
