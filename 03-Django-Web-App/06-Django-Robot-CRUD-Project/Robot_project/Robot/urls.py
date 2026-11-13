from django.urls import path
from . import views

urlpatterns = [

    path('robots/', views.robot_list, name='robot_list'),

    path('edit/<int:id>/', views.edit_robot, name='edit_robot'),

    path('delete/<int:id>/', views.delete_robot, name='delete_robot'),

]
