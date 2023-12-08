from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('pecas/', views.pecas, name='pecas'),
    path('addpecas/', views.addpecas, name='addpecas'),
    path('clientes/', views.clientes, name='clientes'),
    path('addclientes/', views.addclientes, name='addclientes'),
    path('mecanicos/', views.mecanicos, name='mecanicos'),
    path('addmecanicos/', views.addmecanicos, name='addmecanicos'),
    path('veiculos/', views.veiculos, name='veiculos'),
    path('addveiculos/', views.addveiculos, name='addveiculos'),
    path('equipes/', views.equipes, name='equipes'),
    path('addequipes/', views.addequipes, name='addequipes'),
    path('addordemservico/', views.addordemservico, name='addordemservico'),
    path('listaordensservico/', views.listaordensservico, name='listaordensservico'),
    path('logout/', views.logout, name='logout')
]