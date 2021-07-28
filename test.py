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
    department = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# Create table
# Base.metadata.create_all(engine)
if __name__ == '__main___':
    student1 = Student(name="Jone Doe", age="12", grade="4.50", department="CSE")
    student2 = Student(name="Jone One", age="12", grade="4.50")
    student3 = Student(name="Jone Two", age="12", grade="4.50")

    # Single Insert
    session.add(student1)
    session.add_all([student2, student3])

    session.commit()
