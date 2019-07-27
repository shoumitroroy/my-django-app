from django import forms
from myapp.models import Student,Employee

#it's no use any model class
class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    date=forms.DateTimeField(label="Enter date: ")

#this form create from model class
class StuForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class StudentFormUpload(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 10)
    email     = forms.EmailField(label="Enter Email")
    file      = forms.FileField() # for creating file input