from django.urls import path
from . import views

urlpatterns = [
    # path('videcall/<str:room_name>/', views.call_view, name='call_view'),
    path('call/',views.videocall, name='call'),
]
