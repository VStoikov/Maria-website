from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	FormView
)
from .models import Post, Page, Services
from newsletter.forms import JoinForm

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
