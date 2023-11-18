from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Course, Lesson, Test, UserCourseProgress

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource

admin.site.register(Course, CourseAdmin)


class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson 

class LessonAdmin(ImportExportModelAdmin):
    resource_class = LessonResource

admin.site.register(Lesson, LessonAdmin)

class TestResource(resources.ModelResource):
    class Meta:
        model = Test

class TestAdmin(ImportExportModelAdmin):
    resource_class = TestResource

admin.site.register(Test, TestAdmin)

admin.site.register(UserCourseProgress)
