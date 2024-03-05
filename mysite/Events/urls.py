from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.database, name='home'),
    path('e/', views.database1, name='Events'),
    path('', views.index, name='index'),

]
