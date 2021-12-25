from rest_framework import serializers
from domain.models.school import School
from school.serializers.student_serializer import StudentDetailsSerializer


class SchoolSerializer(serializers.ModelSerializer):
    def validate(self, data):
        request_method = self.context.get('request').method
        if request_method == 'PUT' or request_method == 'PATCH':
            '''check if the schools given max student number is greater the total student'''
            if data.get('max_number_of_student') < self.instance.associate_student.count():
                raise serializers.ValidationError("Max number of student should be greater then total number of"
                                                  " students")
        return data

    class Meta:
        model = School
        fields = '__all__'


class SchoolDetailsSerializer(serializers.ModelSerializer):
    associate_student = StudentDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'
