from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:pk>', views.post, name='posts'),
    path('contactform', views.contactform, name='contactform'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('createform', views.createform, name='createform'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('delcon/<str:sk>', views.delcon, name='delcon')
]
