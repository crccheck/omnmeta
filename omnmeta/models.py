from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy import Column, Integer, String


class Base(object):
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def __repr__(cls):
        if hasattr(cls, '__unicode__'):
            return cls.__unicode__()
        else:
            return cls.__name__


Base = declarative_base(cls=Base)


class File(Base):
    path = Column(String(300), nullable=False)
    hash = Column(String(16))  # md5sum
