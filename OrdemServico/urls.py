from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('pecas/', views.pecas, name='pecas'),
    path('addpecas/', views.addpecas, name='addpecas'),

]