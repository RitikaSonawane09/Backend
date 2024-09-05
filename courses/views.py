from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Course, CourseInstance
from .serializers import CourseSerializers , CourseInstanceSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    
    if serializer.is_valid():
        course_code = serializer.validated_data.get('course_code')
        
       
        if Course.objects.filter(course_code=course_code).exists():
            return Response({'success': False, 'message': 'Course already exists.'}, status=400)
        
    
        serializer.save()
        return Response({'success': True, 'message': 'Course added successfully.'}, status=201)
    
    return Response({'success': False, 'message': 'Validation failed.', 'errors': serializer.errors}, status=400)

@api_view(['GET'])
def get_instances_by_year_and_semester(request):
    year = request.query_params.get('year')
    semester = request.query_params.get('semester')
    instances = CourseInstance.objects.filter(year=year, semester=semester)
    serializer = CourseInstanceSerializer(instances, many=True)
    return Response(serializer.data)


class CourseDeleteByCodeView(APIView):
    def delete(self, request, course_code):
        try:
            course = Course.objects.get(course_code=course_code)
            course.delete()
            return Response({'success': True, 'message': 'Course deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({'success': False, 'message': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
   


class CourseInstanceListCreateView(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
    def get_queryset(self):
        queryset = CourseInstance.objects.all()
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')

        if year is not None:
            queryset = queryset.filter(year=year)
        if semester is not None:
            queryset = queryset.filter(semester=semester)

        return queryset




class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer
    lookup_field = 'course_id'

    def get_queryset(self):
        course_title=self.kwargs['course']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter( year=year, semester=semester, course__code=self.kwargs['course_code'])
        try:
            return CourseInstance.objects.get(  year=year, semester=semester,)
        except CourseInstance.DoesNotExist:
            raise Http404

class CourseInstanceViewSet(viewsets.ModelViewSet):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer