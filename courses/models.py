from django.db import models

class Course(models.Model):  
    course_name = models.CharField(max_length=1000, unique=True, blank=False)
    course_code = models.CharField(max_length=50, unique=True, blank=False)
    course_description = models.TextField(blank=False)

    def __str__(self):
        return f'{self.course_code} - {self.course_name}'

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, related_name='instances', blank=False, on_delete=models.CASCADE) 
    year = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
        unique_together = ('course', 'year', 'semester', )

    def __str__(self):
        return f'{self.course} ({self.year} - Semester {self.semester})'
