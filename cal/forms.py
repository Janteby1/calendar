from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput
from .models import UserProfile, Events, Organization, Tags, TaggedTag


# form used to register a user
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            "name",
            "username",
            "password",
            "email",
            "phone", 
            "website",
            "industry"
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }


class OrgLoginForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            "username",
            "password",
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }





        