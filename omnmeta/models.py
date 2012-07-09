from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy import Column, Integer, String


class Base(object):
    """
    sqlalchemy base class

    Provides a primary key field, __tablename__, and __repr__

    """
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        if hasattr(self, '__unicode__'):
            return self.__unicode__()
        else:
            return "<%s Object>" % self.__class__.__name__


Base = declarative_base(cls=Base)


class SomeFile(Base):
    """
    The basic unit. Represents a file located on disk.

    The ``path`` is the last known path to the file. The ``hash`` is the
    md5sum of the file contents used to check the uniqueness of the file.

    """
    name = Column(String())
    path = Column(String(300), nullable=False, unique=True)
    hash = Column(String(16))  # md5sum

    def __unicode__(self):
        return self.path
