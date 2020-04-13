from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
    AboutView,
    ServicesView,
    #HaircutsView,
    ContactsView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('services/', ServicesView.as_view(), name='blog-services'),
    path('contacts/', ContactsView.as_view(), name='blog-contacts'),
    #path('about/', views.about, name='blog-about'),
]