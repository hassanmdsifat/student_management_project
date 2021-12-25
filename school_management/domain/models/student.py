import uuid
from django.db import models
from domain.models.timestamp import TimeStamp

from domain.models.school import School


MALE_CHOICE = 'm'
FEMALE_CHOICE = 'f'
OTHER_CHOICE = 'o'

gender_choices = [
    (MALE_CHOICE, 'M'),
    (FEMALE_CHOICE, 'F'),
    (OTHER_CHOICE, 'O')
]


class Student(TimeStamp):
    school = models.ForeignKey(School, related_name='associate_student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=5, choices=gender_choices, default=OTHER_CHOICE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        db_table = 'student'
