from django.urls import path
from . import views



urlpatterns = [
path('', views.recipepost, name='recipepost'),
path('cpost', views.cpost, name='cpost'),
path('dpost/<int:d_id>/', views.dpost, name='dpost'),
]

