from django.db import models
from domain.models.timestamp import TimeStamp


class School(TimeStamp):
    name = models.CharField(max_length=20)
    max_number_of_student = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'school'
