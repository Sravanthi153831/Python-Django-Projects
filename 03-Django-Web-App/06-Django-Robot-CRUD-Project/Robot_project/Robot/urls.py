from django.urls import path
from . import views

urlpatterns = [

    path('', views.robot_list, name='robot_list'),

    path('edit/<int:id>/', views.edit_robot, name='edit_robot'),

    path('delete/<int:id>/', views.delete_robot, name='delete_robot'),

    path('battery-live/', views.battery_live, name='battery_live'),

]
