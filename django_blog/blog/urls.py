from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path('login/', LoginViews.as_view(template_name='blog/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutViews.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
