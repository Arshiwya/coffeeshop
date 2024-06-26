from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import User, Contact


class SignUserForm(forms.ModelForm):
    password2 = forms.CharField(required=True, max_length=255)

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message", "status"]
