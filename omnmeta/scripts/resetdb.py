#! /usr/bin/env python
from _fixpath import *

import os

from sqlalchemy import create_engine

from omnmeta import settings
from omnmeta.settings import project_dir
from omnmeta.models import Base

# delete old database
db_path = project_dir(settings.DB_FILENAME)
if os.path.isfile(db_path):
    os.unlink(db_path)

# create new database
engine = create_engine(settings.DB, echo=True)
Base.metadata.create_all(engine)
