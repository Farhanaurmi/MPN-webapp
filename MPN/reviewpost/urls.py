
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviewpost, name='reviewpost'),
    path('creviewpost', views.creviewpost, name='creviewpost'),
    #path('dreviewpost/<int:d_id>/', views.dreviewpost, name='dreviewpost'),
    path('mypostd/<int:m_id>/', views.mypostd, name='mypostd'),
    path('mypost/', views.mypost, name='mypost'),
    path('mypostd/<int:m_id>/delete', views.mypostdelete, name='mypostdelete'),
]