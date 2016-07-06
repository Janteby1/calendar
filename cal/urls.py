from django.conf.urls import include, url
from django.contrib import admin
from cal import views #gets all our view functions

urlpatterns = [
    # url(r'^$', views.Landing.as_view(), name='landing'),
    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^user_register$', views.User_Register.as_view(), name='user_register'),
    url(r'^user_login$', views.User_Login.as_view(), name='user_login'),
    url(r'^org_register$', views.Org_Register.as_view(), name='org_register'),
    # url(r'^org_login$', views.Org_Login.as_view(), name='org_login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),

    url(r'^add$', views.AddEvent.as_view(), name='add'),
    url(r'^all$', views.ViewAll.as_view(), name='all'),
    # url(r'^category$', views.SearchDate_Category.as_view(), name='search_category'),
    # url(r'^area$', views.SearchDate_Area.as_view(), name='search_area'),

    # # # here we send the url to the views with the slug id attached to it
    # # url(r'^edit/(?P<dates_slug>[A-Za-z0-9\-\_]+)$', views.Edit_Date.as_view(), name="edit"),
    url(r'^delete/(?P<events_id>[A-Za-z0-9\-\_]+)$', views.Delete_Event.as_view(), name='delete'),
    url(r'^vote_up/(?P<events_id>[A-Za-z0-9\-\_]+)$', views.Vote_Up_Event.as_view(), name='vote_up'),
    url(r'^vote_down/(?P<events_id>[A-Za-z0-9\-\_]+)$', views.Vote_Down_Event.as_view(), name='vote_down'),
    url(r'^tags/(?P<event_id>[A-Za-z0-9\-\_]+)$', views.AddTags.as_view(), name='tags'),

    url(r'^my$', views.My_Events.as_view(), name='my'),
    url(r'^my_tags$', views.My_Tags.as_view(), name='my_tags'),
]