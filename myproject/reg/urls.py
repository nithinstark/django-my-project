from django.urls import path
from reg import views


urlpatterns =[
    path('register/', views.reg),
]