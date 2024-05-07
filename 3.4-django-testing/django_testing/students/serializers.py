from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):

        if len(Course.objects.filter(name=self.context["request"].students)) >= 20:
            raise ValidationError('На курсе максимальное число студентов')

        return data
