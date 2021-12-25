from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from domain.models.school import School
from domain.models.student import Student
from package.helpers.school_helper import SchoolHelper


class SchoolTest(APITestCase):
    def setUp(self):
        self.all_schools = SchoolHelper().create_fake_schools()

    def test_school_create(self):
        test_cases = [
            {
                'data': {
                    'name': 'TEST School',
                    'max_number_of_students': 2
                },
                'result': status.HTTP_201_CREATED
            },
            {
                'data': {
                    'name': 'TEST School',
                    'max_number_of_student': -12
                },
                'result': status.HTTP_400_BAD_REQUEST
            },
            {
                'data': {
                    'name': '',
                    'max_number_of_student': 10
                },
                'result': status.HTTP_400_BAD_REQUEST
            },
            {
                'data': {
                    'name': 'Hello My Name is School',
                    'max_number_of_student': 10
                },
                'result': status.HTTP_400_BAD_REQUEST
            }
        ]
        url = reverse('school-list')
        for case in test_cases:
            response = self.client.post(url, case['data'], format='json')
            self.assertEqual(response.status_code, case['result'])

    def test_school_list(self):
        url = reverse('school-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_school(self):
        school_object = self.all_schools[0]
        test_case = [
            {
                'id': self.all_schools[0].id,
                'data': {
                    'name': school_object.name,
                    'max_number_of_student': 30,
                },
                'status': status.HTTP_200_OK
            },
            {
                'id': self.all_schools[2].id,
                'data': {
                    'name': '',
                    'max_number_of_student': 30,
                },
                'status': status.HTTP_400_BAD_REQUEST
            },
            {
                'id': 20000,
                'data': {
                    'name': 'No School',
                    'max_number_of_student': 30,
                },
                'status': status.HTTP_404_NOT_FOUND
            },
            {
                'id': self.all_schools[20].id,
                'data': {
                },
                'status': status.HTTP_400_BAD_REQUEST
            }
        ]
        for case in test_case:
            url = reverse('school-detail', kwargs={'pk': case['id']})
            response = self.client.put(url, case['data'], format='json')
            self.assertEqual(response.status_code, case['status'])

    def test_update_school_max_limit(self):
        school_object = self.all_schools[2]
        '''update school max number to 3'''
        school_data = {
            'name': 'Testing School One',
            'max_number_of_student': 3
        }
        url = reverse('school-detail', kwargs={'pk': school_object.id})
        self.client.put(url, school_data, format='json')

        '''create 3 student for school 3'''
        Student.objects.bulk_create([
            Student(first_name='hello', last_name='one', school=school_object),
            Student(first_name='hello', last_name='two', school=school_object),
            Student(first_name='hello', last_name='three', school=school_object)
        ])

        '''updating school max number to 2 will give error'''
        school_data = {
            'name': 'Testing School',
            'max_number_of_student': 2
        }
        url = reverse('school-detail', kwargs={'pk': school_object.id})
        response = self.client.put(url, school_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        '''updating school max number to 5 will give error'''
        school_data = {
            'name': 'Testing School',
            'max_number_of_student': 5
        }
        url = reverse('school-detail', kwargs={'pk': school_object.id})
        response = self.client.put(url, school_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_school(self):
        test_case = [
            {
                'id': self.all_schools[0].id,
                'status': status.HTTP_204_NO_CONTENT
            },
            {
                'id': 2000,
                'status': status.HTTP_404_NOT_FOUND
            }
        ]
        for case in test_case:
            url = reverse('school-detail', kwargs={'pk': case['id']})
            response = self.client.delete(url, format='json')
            self.assertEqual(response.status_code, case['status'])


class StudentTest(APITestCase):
    def setUp(self):
        self.all_schools = SchoolHelper().create_fake_schools()

    def test_create_student(self):
        test_case = [
            {
                'data': {
                    'first_name': 'Sifat',
                    'last_name': 'Hassan',
                    'school': self.all_schools[0].id
                },
                'status': status.HTTP_201_CREATED
            },
            {
                'data': {
                    'first_name': 'Sifat',
                    'last_name': '',
                    'school': self.all_schools[0].id
                },
                'status': status.HTTP_400_BAD_REQUEST
            },
            {
                'data': {
                    'first_name': 'Sifat',
                    'last_name': '',
                },
                'status': status.HTTP_400_BAD_REQUEST
            },
            {
                'data': {
                    'first_name': 'Sifat',
                    'last_name': 'Hassan 2',
                    'date_of_birth': '2020-01-03',
                    'school': self.all_schools[0].id
                },
                'status': status.HTTP_201_CREATED
            }
        ]
        for case in test_case:
            url = reverse('student-list')
            response = self.client.post(url, case['data'], format='json')
            self.assertEqual(response.status_code, case['status'])

    def test_update_student(self):
        student_objects = Student.objects.bulk_create([
            Student(first_name='hello', last_name='one', school=self.all_schools[1]),
            Student(first_name='hello', last_name='two', school=self.all_schools[2]),
            Student(first_name='hello', last_name='three', school=self.all_schools[3])
        ])

        test_case = [
            {
                'id': student_objects[0].id,
                'data': {
                    'first_name': 'Test',
                    'last_name': 'Hassan',
                    'date_of_birth': '2020-01-01',
                    'school': student_objects[0].school.id
                },
                'status': status.HTTP_200_OK
            },
            {
                'id': student_objects[0].id,
                'data': {
                    'first_name': 'Test',
                    'last_name': 'Hassan',
                    'date_of_birth': '2020-01-01',
                },
                'status': status.HTTP_400_BAD_REQUEST
            },
            {
                'id': student_objects[2].id,
                'data': {
                    'first_name': 'Test',
                    'last_name': '',
                    'date_of_birth': '2020-01-01',
                    'school': self.all_schools[5].id
                },
                'status': status.HTTP_400_BAD_REQUEST
            },
            {
                'id': student_objects[2].id,
                'data': {
                    'first_name': 'Test',
                    'last_name': 'TEST',
                    'date_of_birth': '2020-01-01',
                    'school': self.all_schools[5].id
                },
                'status': status.HTTP_200_OK
            },
            {
                'id': 3000,
                'data': {
                    'first_name': 'Test',
                    'last_name': 'TEST',
                    'date_of_birth': '2020-01-01',
                    'school': self.all_schools[5].id
                },
                'status': status.HTTP_404_NOT_FOUND
            }
        ]
        for case in test_case:
            url = reverse('student-detail', kwargs={'pk': case['id']})
            response = self.client.put(url, case['data'], format='json')
            self.assertEqual(response.status_code, case['status'])

    def test_update_student_check_max_limit(self):
        school_object_one = School.objects.create(name='Primary School', max_number_of_student=3)
        school_object_two = School.objects.create(name='Primary School 2', max_number_of_student=3)
        student_objects = Student.objects.bulk_create([
            Student(first_name='hello', last_name='one', school=school_object_one),
            Student(first_name='hello', last_name='two', school=school_object_one),
            Student(first_name='hello', last_name='three', school=school_object_one)
        ])
        test_case = [
            {
                'type': 'create',
                'id': None,
                'data': {
                    'first_name': 'hello',
                    'last_name': 'four',
                    'school': school_object_one.id
                },
                'status': status.HTTP_400_BAD_REQUEST,
            },
            {
                'type': 'update',
                'id': student_objects[0].id,
                'data': {
                    'first_name': 'hello',
                    'last_name': 'five',
                    'school': school_object_two.id
                },
                'status': status.HTTP_200_OK,
            },
            {
                'type': 'create',
                'id': None,
                'data': {
                    'first_name': 'hello',
                    'last_name': 'six',
                    'school': school_object_one.id
                },
                'status': status.HTTP_201_CREATED,
            },
            {
                'type': 'create',
                'id': None,
                'data': {
                    'first_name': 'hello',
                    'last_name': 'seven',
                    'school': school_object_one.id
                },
                'status': status.HTTP_400_BAD_REQUEST,
            },
        ]
        for case in test_case:
            if case['type'] == 'create':
                url = reverse('student-list')
                response = self.client.post(url, case['data'], format='json')
            else:
                url = reverse('student-detail', kwargs={'pk': case['id']})
                response = self.client.put(url, case['data'], format='json')
            self.assertEqual(response.status_code, case['status'])

