from test import Student, session

print("Deleting data data")
student = session.query(Student).filter(Student.department == 'CSE').first()
session.delete(student)
session.commit()
