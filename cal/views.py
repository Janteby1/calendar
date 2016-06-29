from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserForm, UserLoginForm, AddEventForm, OrgForm #OrgLoginForm, 
from .models import UserProfile, Events, Organization, Tags, TaggedTag


# Create your views here.
class Landing(View):
    def get(self, request):
        return render(request, "landing.html")

class Index(View):
    def get(self, request):
        user_creation_form = UserForm()
        user_login_form = UserLoginForm()
        org_creation_form = OrgForm()
        add_event_form = AddEventForm()
        # org_login_form = OrgLoginForm()

        # search_date_form_category = SearchDateForm_Category()
        # search_date_form_area = SearchDateForm_Area()
        # search_date_form_price = SearchDateForm_Price()

        context = {
            'user_creation_form': user_creation_form,
            'user_login_form': user_login_form,
            "org_creation_form": org_creation_form,
            "add_event_form": add_event_form,
            # "org_login_form": org_login_form

        #     "search_date_form_category":search_date_form_category,
        #     "search_date_form_area":search_date_form_area,
        #     "search_date_form_price": search_date_form_price,
        }

        return render(request, "index.html", context)


class User_Register(View):
    def post(self, request):
        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)

        user_form = UserForm(data)
        if user_form.is_valid():
            user = user_form.save()
            return JsonResponse({"Message": "Register succesfull", "success": True})
        else:
            return JsonResponse ({"response":"Invalid information", 'success' : False, 'errors': user_form.errors })


class User_Login(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.set_expiry(30000)
            return JsonResponse({"username":user.username, "success": True})
        else:
            return JsonResponse({'errors': form.errors})


class Org_Register(View):
    def post(self, request):
        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)

        if request.user.is_authenticated():
            form = OrgForm(request.POST)
            form.is_valid()
            # add the user to each organization 
            user = request.user
            org = form.save(commit=False)
            org.admin = user
            org.save()
            return JsonResponse({"Message":"added organization", "success": True})
        else:
            return JsonResponse({"success": False})



# class Org_Register(View):
#     def post(self, request):
#         if request.is_ajax():
#             data = request.POST
#         else:
#             body = request.body.decode()
#             if not body: 
#                 return JsonResponse ({"response":"Missing Body"})
#             data = json.loads(body)

#         org_form = OrgForm(data)
#         if org_form.is_valid():
#             org = org_form.save()
#             return JsonResponse({"Message": "Register succesfull", "success": True})
#         else:
#             return JsonResponse ({"response":"Invalid information", 'success' : False, 'errors': org_form.errors })


# class Org_Login(View):
#     def post(self, request):
#         form = OrgLoginForm(request, data=request.POST)
#         print("not valid")
        
#         if form.is_valid():
#             print("valid")
#             Organization = form.get_user()
#             print (Organization)

#             login(request, Organization)
#             request.session.set_expiry(30000)
#             return JsonResponse({"username":Organization.username, "success": True})
#         else:
#             return JsonResponse({'errors': form.errors})


class Logout(View):
    def post(self, request):
        print(request)
        logout(request) # django built in logout 
        return JsonResponse ({"Message":"Logout Successful"})


class AddEvent(View):
    def post(self, request):
        # checks to make sure the user is logged in 
        if request.user.is_authenticated():
            form = AddEventForm(request.POST)
            form.is_valid()
            # add the user to each post 
            user = request.user
            event = form.save(commit=False)
            event.creator = user
            event.save()
            return JsonResponse({"Message":"added date", "success": True})
        else:
            return JsonResponse({"success": False})


class ViewAll(View):
    def get(self, request):
        # this line gets the top 25 events that we have in the db and orders them by top votes
        events = Events.objects.filter(show=True).order_by('-created_at')[:25]
        # put all the values into a json dictionary with a method called from the models
        events = [event.to_json() for event in events]
        print (events)
        return JsonResponse({"success": True, 'results': events})


class Delete_Date(View):
    def post(self, request, events_id=None):
        event = Events.objects.get(id=events_id)

        if request.user.is_authenticated():
            event.show = False
            event.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})


class Vote_Up_Date(View):
    def post(self, request, events_id=None):
        event = Events.objects.get(id=events_id)

        if request.user.is_authenticated():
            event.vote += 1
            event.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})


class Vote_Down_Date(View):
    def post(self, request, events_id=None):
        event = Events.objects.get(id=events_id)

        if request.user.is_authenticated():
            event.vote -= 1
            event.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})

class AddTags(View):
    def get(self, request):
        pass







