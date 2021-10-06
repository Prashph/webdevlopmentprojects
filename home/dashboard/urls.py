from django.contrib import admin
from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('',index,name="index" ),
    path('details/',details,name="details" ),
    path('services/',myservices,name="details" ),
    path('contact/',contactus,name="contactus" ),
    path('login/',loginUser,name="loginUser" ),
    path('logout/',logoutUser,name="logoutUser" ),




]