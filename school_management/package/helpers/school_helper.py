from faker import Faker
from domain.models.school import School


class SchoolHelper:
    def __init__(self):
        self.factory = Faker()

    def create_fake_schools(self):
        school_dictionary = []
        for _ in range(21):
            school_dictionary.append(School(name=self.factory.word(),
                                            max_number_of_student=self.factory.random_int(0, 200)))
        objs = School.objects.bulk_create(school_dictionary)
        return objs
