from django.contrib import admin

from course.models import Course

from course.models import Subject, Student, Tutor
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title","slug"]

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["title","image_tag"]

admin.site.register(Subject,SubjectAdmin)


admin.site.register(Student)

admin.site.register(Tutor)