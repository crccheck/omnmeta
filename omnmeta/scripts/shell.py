# loads models into a REPL like ipython

from _fixpath import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from omnmeta import settings

engine = create_engine(settings.DB, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

from omnmeta.models import *
