#! /usr/bin/env python
# loads models into a REPL like ipython

import os
import sys

# cheat to make imports work without needed to change path,
paths = [
    os.path.join(os.path.dirname(__file__), '..', '..'),
]
sys.path = paths + sys.path
del paths

from omnmeta.models import *

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
