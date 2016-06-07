from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone #make sure to set the timezone 

# Create your models here.
class Events(models.Model):
	date = models.CharField (max_length=120)
    place = models.CharField (max_length=120)
    address = models.CharField (max_length=150)
    description = models.CharField (max_length=280)

    phone = models.CharField (max_length=20, null = True, default = None,)
    website = models.URLField(max_length=120, null = True, default = None,) 
    price = models.CharField (max_length=5, null = True, default = None,)

    created_at = models.DateTimeField(default = timezone.now, editable=False)
    show = models.BooleanField(default=True)
    vote = models.IntegerField(default = 0)

    def to_json(self):
        return {
            "id": self.id,
            "place": self.place,
            "date": self.date,
            "address": self.address,
            "description": self.description,
            "phone": self.phone,
            "website": self.website,
            "price": self.price,
            "created_at": self.created_at,
            "vote": self.vote,
            "show": self.show,
        }


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    '''
    Included in the django user model are these attributes:
    Username, Password, Email address, firstname, surname
    '''
    def to_json(self):
        return {
            "id": self.id,
            "Username": self.Username,
            "firstname": self.firstname,
        }


class Organization(models.Model):
	name = models.CharField (max_length=120)
    username = models.CharField (max_length=120)
    password = models.CharField (max_length=150)
    email = models.EmailField (max_length=280)
    phone = models.CharField (max_length=120)
    website = models.URLField (max_length=150)
    industry = models.CharField (max_length=120)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "website": self.website,
        }


class Tags(models.Model):
	name = models.CharField (max_length=120)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }










