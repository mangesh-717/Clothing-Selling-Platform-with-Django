from django.contrib import admin
from django.urls import path
from .views import *
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home,name='home'),
    path('fruits/',Sweetfruits,name='fruits'),
    path('vegetables/',vegetabalesfun,name='vegetables'),
    path('Cart/',Cart,name='cart'),
    path('contact_us/',help,name='contact_us'),
    path('signup/',signup, name='register'),
    path('login/',login_form, name='loginform'),
    path('updation_of_user/',updations_of_user, name='updation'),
    path('ordered/',Ordered, name='ordered')
]
