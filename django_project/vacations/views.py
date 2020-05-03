from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from .models import Vacations
from .forms import VacationsForm
from django.contrib import messages
from django.contrib.auth.models import Group


def employee(request):
	group_name=Group.objects.all()
	group_name=str(group_name[0])
	if "Employee" == group_name:
		user_name=request.user.get_username()

		#Getting all Post and Filter By Logged UserName
		vacations_list = Vacations.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q")
		if q:
			vacations_list=vacations_list.filter(vacations_with__icontains=q)
		else:
			vacations_list = vacations_list

		vacations= {
		    "query": vacations_list,
		    "user_name":user_name
		}
		return render(request, 'vacations/employee.html', vacations )
	else:
		return redirect('http://localhost:8000/') 

def employee_vacations_list(request):
	group_name=Group.objects.all().filter(user = request.user)
	group_name=str(group_name[0])
	if "Employee" == group_name:
		user_name=request.user.get_username()

		#Getting all Post and Filter By Logged UserName
		vacations_list = Vacations.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			vacations_list=vacations_list.filter(date__icontains=q)
		else:
			vacations_list = vacations_list

		vacations= {
		    "query": vacations_list,
		    "user_name":user_name,
		    "form":VacationsForm(),
		}
		form = VacationsForm(request.POST or None)
		if form.is_valid():
			    saving=form.save(commit=False)
			    saving.user=request.user
			    saving.save()
			    messages.success(request, 'Периодът за почивка беше добавен успешно.')
		return render(request, 'vacations/employee_create_vacations.html', vacations )
	else:
		return redirect('http://localhost:8000/')

  
def vacations_delete(request, id):
	group_name=Group.objects.all().filter(user = request.user)
	group_name=str(group_name[0])
	if "Employee" == group_name:
		single_vacations= Vacations.objects.get(id=id)
		single_vacations.delete()
		messages.success(request, 'Периодът за беше изтрит успешно.')
		return redirect('http://localhost:8000/vacations/create_vacations/')
	else:
		return redirect('http://localhost:8000/')

def employee_vacations_update(request,id):
	group_name=Group.objects.all().filter(user = request.user)
	group_name=str(group_name[0])
	if "Employee" == group_name:
		user_name=request.user.get_username()

		#Getting all Post and Filter By Logged UserName
		vacations_list = Vacations.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q")
		if q:
			vacations_list=vacations_list.filter(date__icontains=q)
		else:
			vacations_list = vacations_list

		single_vacations = Vacations.objects.get(id=id)
		form = VacationsForm(request.POST or None, instance=single_vacations)
		if form.is_valid():
			    saving=form.save(commit=False)
			    saving.user=request.user
			    saving.save()
			    messages.success(request, 'Периодът на почивка беше променен успешно.')
			    return redirect('http://localhost:8000/vacations/create_vacations/')
			    

		vacations= {
		    "query": vacations_list,
		    "user_name":user_name,
		    "form":form,
		}

		return render(request, 'vacations/employee_vacations_update.html', vacations )
	else:
		return redirect('http://localhost:8000/')