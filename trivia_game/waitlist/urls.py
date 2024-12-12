from django.urls import path
from . import views

urlpatterns = [
    path('',views.waitlist,name='waitlist'),
]