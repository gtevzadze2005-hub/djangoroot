from django.db import models

# Create your models here.
class Lecturer(models.Model):
    Lecturer_name = models.CharField(max_length=100)


class Courses(models.Model):
    course_name = models.CharField(max_length=100)

    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE, blank=True, null=True)



class Students(models.Model):
    name = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=2,decimal_places=0)
    year = models.IntegerField(max_length=2)
    active_status = models.BooleanField(default=True)
    bio = models.TextField(blank=True,null=True)

    courses = models.ManyToManyField(Courses)
