from .. import settings
from ..settings import project_dir

from .models import *

# TEST CONFIGURATION
TEST_DB_NAME = "_test.sqlite"


def setup():
    import os

    from sqlalchemy import create_engine

    from ..models import Base

    test_db_path = project_dir(TEST_DB_NAME)
    os.unlink(test_db_path)
    settings.DB = 'sqlite:///%s' % test_db_path
    engine = create_engine(settings.DB, echo=False)
    Base.metadata.create_all(engine)


def teardown():
    # test DB purposely not deleted
    pass
