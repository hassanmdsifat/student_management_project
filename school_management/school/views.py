from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework import filters
from domain.models.school import School
from domain.models.student import Student
from school.serializers.school_serializer import SchoolSerializer, SchoolDetailsSerializer
from school.serializers.student_serializer import StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = School.objects.prefetch_related('associate_student').all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'max_number_of_student']
    ordering_fields = ['name', 'max_number_of_student']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return SchoolDetailsSerializer
        return SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer
    queryset = Student.objects.select_related('school').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gender', 'school']
    search_fields = ['first_name', 'last_name', 'school__name']
    ordering_fields = ['first_name', 'last_name', 'date_of_birth']
