from django import forms
from django.core import validators
from . models import User


class RegistrationForm(forms.ModelForm):
    semester = forms.IntegerField(
        min_value=1, max_value=8, widget=forms.NumberInput(attrs={
            "placeholder": "1-8",
            "class": "form-control",
        }))

    class Meta:
        model = User
        fields = '__all__'
        labels = {
            "name": "Name",
            "f_name": "Father Name",
            "address": "Address",
            "department": "Department",
            "semester": "semester",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your name"
            }),
            "f_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Father Name"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Address"
            }),
            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Department"
            }),
        }
        error_messages = {
            "name": {
                "required": "Name should not be empty",
            },
        }
