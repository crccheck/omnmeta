from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
