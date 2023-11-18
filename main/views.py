from rest_framework import viewsets
from .models import Course, Lesson, Test, UserCourseProgress 
from .serializers import CourseSerializer, LessonSerializer, TestSerializer, UserCourseProgressSerializer
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users")
    else:
        form = RegisterForm()
    return render(request, "home.html", {"form": form})




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class UserCourseProgressViewSet(viewsets.ModelViewSet):
    queryset = UserCourseProgress.objects.all()
    serializer_class = UserCourseProgressSerializer


def home(request):
    return render (request, 'home.html')
