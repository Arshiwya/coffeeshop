from django import forms
from .models import User, Contact
from django.contrib.auth.forms import PasswordResetForm



class SignUserForm(forms.ModelForm):
    password2 = forms.CharField(required=True, max_length=255)

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message", "status"]

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("User with this email does not exist")
        return email