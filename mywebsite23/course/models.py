from django.db import models
from django.utils.safestring import mark_safe

from mywebsite23.home.models import Language, Setting


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False,upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title



class Subject(models.Model):
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to='images/')
    price = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'





class Student(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to='images/')

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to='images/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# class Language(models.Model):
#     name = models.CharField(max_length=20)
#     code = models.CharField(max_length=5)
#     status = models.BooleanField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
# llist = Language.objects.all()
# list1 = []
# for rs in llist:
#     list1.append((rs.code, rs.name))
# langlist = (list1)
#
#
# class Subjectlang(models.Model):
#     setting = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     lang = models.CharField(max_length=6, choices=langlist)
#     title = models.CharField(max_length=100)
#     subject_tutor = models.CharField(max_length=100)
#     description = models.TextField(max_length=500)
#     image = models.ImageField(null=False, upload_to='images/')
#     price = models.CharField(max_length=100)
#     detail = models.CharField(max_length=100)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     slug = models.SlugField(null=False)
#
#     def __str__(self):
#         return self.title
#
#     def image_tag(self):
#         return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
#     image_tag.short_description = 'Image'