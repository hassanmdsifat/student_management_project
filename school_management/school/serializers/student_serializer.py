from rest_framework import serializers
from domain.models.student import Student


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['school']


class StudentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        request_method = self.context.get('request').method
        selected_school_object = data.get('school')
        if request_method == 'POST':
            '''check if current selected school have available seats'''
            if selected_school_object.associate_student.count() >= selected_school_object.max_number_of_student:
                raise serializers.ValidationError("No seat available in the selected school")
        else:
            ''' if student switch school, please check if school have available seats'''
            if self.instance.school is not selected_school_object \
                    and selected_school_object.associate_student.count() >= \
                    selected_school_object.max_number_of_student:
                raise serializers.ValidationError("No seat available in the selected school")
        return data

    class Meta:
        model = Student
        fields = '__all__'
