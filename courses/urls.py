from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseInstanceViewSet, CourseListCreateView, CourseDetailView, CourseInstanceListCreateView, CourseInstanceDetailView,CourseDeleteByCodeView
CourseDeleteByCodeView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'instances', CourseInstanceViewSet)

urlpatterns = [
    
    path('', include(router.urls)),

    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/', CourseInstanceListCreateView.as_view(), name='course-instance-list-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='course-instance-list'),
    path('instances/<int:pk>/', CourseInstanceDetailView.as_view(), name='course-instance-detail'),
    path('courses/code/<str:course_code>/', CourseDeleteByCodeView.as_view(), name='course-delete-by-code'),

]
