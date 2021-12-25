from faker import Faker
from domain.models.student import Student


class StudentHelper:
    def __init__(self):
        self.factory = Faker()

    def create_fake_students(self, school_objects):
        school_index = 0
        student_dictionary = []
        current_school_object = school_objects[school_index]
        for i in range(1, 601):
            if i % 30 == 0:
                school_index += 1
                current_school_object = school_objects[school_index]

            if i % 2 == 0:
                gender = 'M'
            else:
                gender = 'F'
            student_profile = self.factory.simple_profile(gender)
            full_name = student_profile.get('name')
            first_name = full_name.split()[0]
            last_name = full_name.split()[1]
            student_dictionary.append(Student(first_name=first_name, last_name=last_name,
                                              date_of_birth=student_profile.get('birthdate'),
                                              gender=student_profile.get('sex'),
                                              school=current_school_object))
        Student.objects.bulk_create(student_dictionary)
