from django import forms
from django.contrib.auth.models import User

from .models import Student, Subject, Grade


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','score']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple,
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {}

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {}

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']