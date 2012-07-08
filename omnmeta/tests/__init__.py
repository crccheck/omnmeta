from .. import settings
from ..settings import project_dir

from .models import *

# TEST CONFIGURATION
TEST_DB_NAME = "_test.sqlite"


def setup():
    # TODO delete TEST_DB
    from sqlalchemy import create_engine
    from ..models import Base
    settings.DB = 'sqlite:///%s' % project_dir(TEST_DB_NAME)
    engine = create_engine(settings.DB, echo=False)
    Base.metadata.create_all(engine)


def teardown():
    # test DB purposely not deleted
    pass
