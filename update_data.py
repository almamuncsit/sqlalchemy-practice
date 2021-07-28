from test import Student, session

print("Updating data")
student = session.query(Student).filter(Student.name == 'Sarkar').first()
student.department = "EEE"

session.commit()
