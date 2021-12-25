from django.core.management.base import BaseCommand
from django.db import transaction
from package.helpers.school_helper import SchoolHelper
from package.helpers.student_helper import StudentHelper


class Command(BaseCommand):
    help = 'Generate Fake School And Students'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                school_objects = SchoolHelper().create_fake_schools()
                StudentHelper().create_fake_students(school_objects)
                self.stdout.write("Generation Complete")
        except Exception as E:
            self.stdout.write(str(E))
