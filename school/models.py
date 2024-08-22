from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Questions(models.Model):
    question = models.TextField()
    email = models.EmailField()

class Teachers(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Licenses(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()

class Awards(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField()

class Admission(models.Model):
    student_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    class_number = models.CharField(max_length=10)
    student_pd = models.CharField(max_length=50)
    parent_pd = models.CharField(max_length=50)