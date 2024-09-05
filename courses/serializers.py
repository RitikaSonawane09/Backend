from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
            model = Course
            fields ='__all__'


class CourseInstanceSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(),)
   
    class Meta:
        model = CourseInstance
        fields ='__all__'
    
