from django.db import models
from classroom.models import Class, Subject
from ckeditor.fields import RichTextField
from .validator import validate_file_extension


class Lecture(models.Model):
    title = models.CharField(max_length=70, unique=True, default='')
    note = models.FileField(upload_to="lecture notes", default="lecture.pdf", validators=[validate_file_extension])
    level = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')
    term = models.IntegerField(default=1)
    timestamp = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} | {self.level} | term {self.term}'

class Course(models.Model):
    title = models.CharField(max_length=30, unique=True)
    link = models.CharField(max_length=400, unique=True)
    poster = models.ImageField(upload_to="course_posters", default="course.jpg")

    def __str__(self):
        return self.title
