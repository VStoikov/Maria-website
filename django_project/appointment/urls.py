from django.urls import path

from .views import(
	employee,
	employee_appointment_list,
	appointment_delete,
	employee_appointment_update,
	)

from . import views

urlpatterns = [
    path('', views.employee, name='employee_home'),
    path('my_appointment/', views.employee, name='employee_appointment'),
    path('create_appointment/', views.employee_appointment_list, name='employee_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', employee_appointment_update,name='employee_appointment_update'),  
]

