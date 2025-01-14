from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('signup/', views.signup, name='signup'),
path('welcome/', views.welcome, name='welcome'),
path('api/leaderboard', views.api_leaderboard, name='api_leaderboard'),
]