from django.urls import path

from .views import(
	employee,
	employee_vacations_list,
	vacations_delete,
	employee_vacations_update,
	)

from . import views

urlpatterns = [
    path('', views.employee, name='employee_home'),
    path('my_vacations/', views.employee, name='employee_vacations'),
    path('create_vacations/', views.employee_vacations_list, name='employee_vacations_list'),
    path('create_vacations/delete/<int:id>/', vacations_delete,name='vacations_delete'),
    path('create_vacations/update/<int:id>/', employee_vacations_update,name='employee_vacations_update'),  
]
