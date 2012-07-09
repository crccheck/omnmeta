from nose.tools import raises
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from omnmeta import settings

from ..models import SomeFile


class TestSomeFileModel:
    def setUp(self):
        print settings.DB
        engine = create_engine(settings.DB, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(SomeFile).delete()
        self.session = session

    def test_can_add(self):
        assert self.session.query(SomeFile).count() == 0
        f = SomeFile(path='/path/to/some/file')
        self.session.add(f)
        self.session.commit()
        assert self.session.query(SomeFile).count() == 1

    @raises(IntegrityError)
    def test_make_sure_path_is_unique(self):
        f = SomeFile(path='/path/to/some/file')
        self.session.add(f)
        f = SomeFile(path='/path/to/some/file')
        self.session.add(f)
        self.session.commit()

    def test_name_is_guessed(self):
        f = SomeFile(path='/path/hello.dolly')
        self.session.add(f)
        self.session.commit()
        assert f.name == 'hello'

    def test_set_name_isnt_overwritten(self):
        f = SomeFile(path='/path/hello.dolly', name='bye')
        self.session.add(f)
        self.session.commit()
        assert f.name == 'bye'
