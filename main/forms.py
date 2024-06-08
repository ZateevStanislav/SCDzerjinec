from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddStudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ['surname', 'name', 'birthdate', 'phone_number']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-input'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-input'}),
        }
