from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, TestViewSet, UserCourseProgressViewSet
from . import views

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'tests', TestViewSet)
router.register(r'user-course-progress', UserCourseProgressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home , name="home"),
    path("register/", views.register, name="register")

]

