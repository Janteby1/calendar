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


# class OrgLoginForm(forms.ModelForm):
#     class Meta:
#         model = Organization
#         fields = [
#             "username",
#             "password",
#         ]
#         widgets = {
#             # this sets the input text area
#             "password": PasswordInput(),
#         }















class AddEventForm(forms.Form):
    date = forms.CharField() # get the input directly from the user
    place = forms.CharField() # get the input directly from the user
    address = forms.CharField() # get the input directly from the user

    price = forms.CharField() # get the input directly from the user
    description = forms.CharField() # get the input directly from the user
    phone = forms.CharField() # get the input directly from the user
    website = forms.CharField() # get the input directly from the user

'''    
    organization = models.ForeignKey(Organization) # FK to the Organization table
    Tags
'''

    # def save(self, commit=True):
    #     date = Dates(**self.cleaned_data)
    #     if commit == True:
    #         date.save()
    #     return date






        