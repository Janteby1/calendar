from django.conf.urls import include, url
from django.contrib import admin
from cal import views #gets all our view functions

urlpatterns = [
    # url(r'^$', views.Landing.as_view(), name='landing'),
    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^user_register$', views.User_Register.as_view(), name='user_register'),
    url(r'^user_login$', views.User_Login.as_view(), name='user_login'),
    url(r'^org_register$', views.Org_Register.as_view(), name='org_register'),
    url(r'^org_login$', views.Org_Login.as_view(), name='org_login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),

    url(r'^add$', views.AddDate.as_view(), name='add'),
    # url(r'^price$', views.SearchDate_Price.as_view(), name='search_price'),
    # url(r'^category$', views.SearchDate_Category.as_view(), name='search_category'),
    # url(r'^area$', views.SearchDate_Area.as_view(), name='search_area'),

    # # # here we send the url to the views with the slug id attached to it
    # # url(r'^edit/(?P<dates_slug>[A-Za-z0-9\-\_]+)$', views.Edit_Date.as_view(), name="edit"),
    # url(r'^delete/(?P<dates_id>[A-Za-z0-9\-\_]+)$', views.Delete_Date.as_view(), name='delete'),
    # url(r'^vote_up/(?P<dates_id>[A-Za-z0-9\-\_]+)$', views.Vote_Up_Date.as_view(), name='vote_up'),
    # url(r'^vote_down/(?P<dates_id>[A-Za-z0-9\-\_]+)$', views.Vote_Down_Date.as_view(), name='vote_down'),
    # url(r'^top$', views.Top_Dates.as_view(), name='top'),
]