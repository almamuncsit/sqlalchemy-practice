from operator import or_

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


# Get all data
students = session.query(Student)
for student in students:
    print(student.name, student.age)

# Get all data
print('\nPrint order by')
students = session.query(Student).order_by(Student.name)
for student in students:
    print(student.name, student.age)

# Filter data
print("\nPrint filtered data data")
students = session.query(Student).filter(or_(Student.name == 'Khan', Student.name == 'Sarkar'))
for student in students:
    print(student.name, student.age)

# Filter data
print("\nPrint single data")
student = session.query(Student).filter(Student.name == 'Khan').first()
print(student.name, student.age)

# Filter data
print("\nPrint filtered data data")
student_count = session.query(Student).filter(or_(Student.name == 'Khan', Student.name == 'Sarkar')).count()
print(student_count)

session.commit()
