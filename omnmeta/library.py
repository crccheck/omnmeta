# TODO add tests, too lazy to do it now since this is dependent on having files
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from . import settings
from .models import SomeFile

engine = create_engine(settings.DB, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def add(path):
    # from pdb4qt import set_trace; set_trace()
    path = str(path)
    f = SomeFile(path=path)
    try:
        instance = session.query(SomeFile).filter_by(path=path).one()
    except NoResultFound:
        session.add(f)
        session.commit()
