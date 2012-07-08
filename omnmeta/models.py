from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy import Column, Integer, String


class Base(object):
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
    path = Column(String(300), nullable=False, unique=True)
    hash = Column(String(16))  # md5sum

    def __unicode__(self):
        return self.path
