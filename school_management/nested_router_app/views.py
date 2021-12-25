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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gender']
    search_fields = ['first_name', 'last_name', 'school__name']
    ordering_fields = ['first_name', 'last_name', 'date_of_birth']

    def get_queryset(self):
        query_params = self.request.query_params
        ordering = query_params.get('ordering', None)
        search_keyword = query_params.get('search', None)
        gender_filter = query_params.get('gender', None)

        student_objects = Student.objects.select_related('school').filter(school_id=self.kwargs['school_pk'])
        if search_keyword:
            student_objects = student_objects.filter(first_name__icontains=search_keyword) |\
                              student_objects.filter(last_name__icontains=search_keyword) |\
                              student_objects.filter(school__name__icontains=search_keyword)
        if gender_filter:
            student_objects = student_objects.filter(gender=gender_filter)
        if ordering:
            student_objects = student_objects.order_by(ordering)
        return student_objects
