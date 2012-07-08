from nose.tools import raises
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from omnmeta import settings

from ..models import File


class TestFileModel:
    def setUp(self):
        print settings.DB
        engine = create_engine(settings.DB, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(File).delete()
        self.session = session

    def test_can_add(self):
        assert self.session.query(File).count() == 0
        f = File(path='/path/to/some/file')
        self.session.add(f)
        self.session.commit()
        assert self.session.query(File).count() == 1

    @raises(IntegrityError)
    def test_make_sure_path_is_unique(self):
        f = File(path='/path/to/some/file')
        self.session.add(f)
        f = File(path='/path/to/some/file')
        self.session.add(f)
        self.session.commit()
