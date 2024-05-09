from django import forms
from datetime import datetime
from datetime import date
from django.forms import ModelForm
from .models import Employee

class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Ім'я")
    last_name = forms.CharField(label="Прізвище")
    date_of_birth = forms.DateField(label="Дата народження",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_enrollment = forms.DateField(label="Дата приєднання",
                                         initial=format(date.today()),
                                         widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class EmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['title', 'abilities', 'position', 'author', 'summary', 'isbn']