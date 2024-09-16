from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('register/',UserCreateView.as_view(),name='user_registration'),
    path('user/<int:pk>/skills/',UserSkillView.as_view(),name='user_skill'),
    path('user/<int:pk>/slot-booking/',SlotCreateView.as_view(),name='slot_booking'),

]
