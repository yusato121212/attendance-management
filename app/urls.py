from django.urls import path
from . import views

urlpatterns = [
    path('',views.attendance_list,name='attendance_list'),
    path('addinwork/<int:pk>/',views.add_in_work,name='add_in_work'),
    path('addoutwork/<int:pk>/',views.add_out_work,name='add_out_work'),
]