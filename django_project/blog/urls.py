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
    ContactsView,
    customer,
    quick_appointmnet,
    appointment_book
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
    path('my_appointment/', views.customer, name='customer-appointment'),
    path('quick_appointmnet/', views.quick_appointmnet, name='quick-appointmnet'),   
    path('update/<int:id>/', views.appointment_book,name='appointment-update'),
    path('team/', views.team, name='team'),
    #path('about/', views.about, name='blog-about'),
]