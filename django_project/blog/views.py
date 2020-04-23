from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	TemplateView
)
from .models import Post, Page, Services
from newsletter.forms import JoinForm
from appointment.models import Appointment
from appointment.forms import AppointmentForm

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class AboutView(CreateView):
	template_name = 'blog/about.html'
	form_class = JoinForm
	title = 'About'
	success_url = '/about'

	def get_context_data(self, *args, **kwargs):
		context = super(AboutView, self).get_context_data(*args, **kwargs)
		context['page_obj'] = Page.objects.all().get(title="За нас")
		return context

class ContactsView(CreateView):
	template_name = 'blog/contacts.html'
	form_class = JoinForm
	title = 'Contacts'
	success_url = '/contacts'

	def get_context_data(self, *args, **kwargs):
		context = super(ContactsView, self).get_context_data(*args, **kwargs)
		context['page_obj'] = Page.objects.all().get(title="Контакти")
		return context

def services(request):
	context = {
		'services': Services.objects.all()
	}
	return render(request, 'blog/services.html', context)

class ServicesView(ListView):
	model = Services
	template_name = 'blog/services.html'
	context_object_name = 'services'

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def team(request):
	group = Group.objects.get(name="Employee")
	employee_list = group.user_set.all()
	return render(request, 'blog/team.html', {'title': 'Team', 'employees': employee_list})

def quick_appointmnet(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Customer" == group_name:
		user_name=request.user.get_username()
		appointment_list = Appointment.objects.all().order_by("-user")
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list# search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name
		}
		return render(request, 'blog/customer_quick_appointment.html', appointments )
	else:
		return redirect('http://localhost:8000/')


def customer(request):#this section for my appointment
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Customer" == group_name:
		user_name=request.user.get_username()#Getting Username
		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(appointment_with=user_name)
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list# search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,    
		}
		return render(request, 'blog/customer_appointment.html', appointments )
	else:
		return redirect('http://localhost:8000/')

def appointment_book(request, id):#activate after clicking book now button
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Customer" == group_name:
		user_name=request.user.get_username()
		single_appointment= Appointment.objects.get(id=id)
		form = single_appointment
		form.appointment_with=user_name
		form.save()
		#return HttpResponseRedirect (instance.get_absolute_url())
		#messages.success(request, 'Your profile was updated.')
		return redirect('http://localhost:8000/my_appointment/')
	else:
		return redirect('http://localhost:8000/')