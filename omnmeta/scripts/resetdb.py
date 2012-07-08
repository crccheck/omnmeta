#! /usr/bin/env python
from _fixpath import *

from sqlalchemy import create_engine

from omnmeta import settings
from omnmeta.models import Base

engine = create_engine(settings.DB, echo=True)
Base.metadata.create_all(engine)
