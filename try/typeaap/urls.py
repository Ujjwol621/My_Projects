from django.urls import path
from typingspeed import views

urlpatterns = [
    path('aboutus', views.about, name='about'),
    path('start', views.start, name='start'),
    path('',views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.custom_login, name='login'),
    path ('signout',views.signout,name='signout'),
    path ('start',views.start,name='start'),
    path ('result',views.result,name='result'),
    path ('leaderboard',views.leaderboard,name='leaderboard'),
]