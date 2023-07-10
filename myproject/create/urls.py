from django.urls import path
from create import views


urlpatterns =[
    path('create/', views.cre, name='cre'),
    path('details/', views.details, name='details'),
]