from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_number = models.PositiveIntegerField()

class Test(models.Model):
    questions = models.TextField()
    correct_answers = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    progress = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set', # Add this line
        related_query_name='custom_user', # Add this line
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set', # Add this line
        related_query_name='custom_user', # Add this line
    )
