from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:root@localhost/sqlalchemy', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    age = Column(Integer)
    grate = Column(String(50))


# Create table
Base.metadata.create_all(engine)
