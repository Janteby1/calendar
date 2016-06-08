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















# Layout
# CHOICES = [('Form name','Database name'),]
# in the form there are two choice that correspond to the same db input (35-64)
STATE_CHOICES = [('ny',"state"), ('nj',"state"), ('other',"state")]
PARKING_CHOICES = [('on',"parking"), ('off',"parking")]
# CATEGORY_CHOICES = CATEGORIES = (('ACT1', "ACT1"), ('ACT2', "ACT2"), ('ACT3', "ACT3"), ('ACT4', "ACT4"), ('ACT5', "ACT5"), ('ACT6', "ACT6"),('ACT7', "ACT7"), ('ACT8', "ACT8"), ('ACT9', "ACT9"), ('ACT10', "ACT10"), ('ACT11', "ACT11"), ('ACT12', "ACT12"), ('ACT13', "ACT13"), ('ACT14', "ACT14"), ('ACT15', "ACT15"), ('ACT16', "ACT16"),('ACT17', "ACT17"), ('ACT18', "ACT18"), ('ACT19', "ACT19"), ('ACT20', "ACT20"), ('ACT21', "ACT21"), ('ACT22', "ACT22"), ('AMU', 'AMU'),('DES', 'DES'),('DES_P', 'DES_P'),('DIN_D', 'DIN_D'),('DIN_Deal', 'DIN_Deal'),('DIN_M', 'DIN_M'),('LUN', 'LUN'),('STA', 'STA'),('WEB', 'WEB'))
CATEGORY_CHOICES = CATEGORIES = (('ACT1', "category"), ('ACT2', "category"), ('ACT3', "category"), ('ACT4', "category"), ('ACT5', "category"), ('ACT6', "category"),('ACT7', "category"), ('ACT8', "category"), ('ACT9', "category"), ('ACT10', "category"), ('ACT11', "category"), ('ACT12', "category"), ('ACT13', "category"), ('ACT14', "category"), ('ACT15', "category"), ('ACT16', "category"),('ACT17', "category"), ('ACT18', "category"), ('ACT19', "category"), ('ACT20', "category"), ('ACT21', "category"), ('ACT22', "category"), ('AMU', 'category'),('DES', 'category'),('DES_P', 'category'),('DIN_D', 'category'),('DIN_Deal', 'category'),('DIN_M', 'category'),('LUN', 'category'),('STA', 'category'),('WEB', 'category'))

class AddDateForm(forms.Form):
    place = forms.CharField() # get the input directly from the user
    address = forms.CharField() # get the input directly from the user
    area = forms.CharField() # get the input directly from the user
    state = forms.ChoiceField(
        choices = STATE_CHOICES,
    )
    category = forms.ChoiceField(
        choices = CATEGORY_CHOICES,
    )
    price = forms.CharField() # get the input directly from the user
    parking = forms.ChoiceField(
        choices = PARKING_CHOICES,
    )
    phone = forms.CharField() # get the input directly from the user
    website = forms.CharField() # get the input directly from the user
    notes = forms.CharField() # get the input directly from the user

    def save(self, commit=True):
        date = Dates(**self.cleaned_data)
        if commit == True:
            date.save()
        return date


        