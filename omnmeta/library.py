# TODO add tests, too lazy to do it now since this is dependent on having files
import hashlib
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
        return instance, False
    except NoResultFound:
        session.add(f)
        session.commit()
        return f, True


def get(filter_args=None):
    # TODO filter
    instance = session.query(SomeFile).all()
    return instance
    # from pdb4qt import set_trace; set_trace()


def update_hashes(*args, **kwargs):
    instance = session.query(SomeFile).filter_by(hash=None)
    for f in instance:
        f.hash = md5_for_file(f.path)
        session.commit()


def md5_for_file(path, block_size=2 ** 20):
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()
