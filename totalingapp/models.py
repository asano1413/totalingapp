from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()

class Subject(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    score = models.FloatField()

    class Meta:
        unique_together = ('student', 'subject')