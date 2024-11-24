from django.urls import path
from . import views

urlpatterns = [
    path('', views.join_waitlist, name='join_waitlist'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]