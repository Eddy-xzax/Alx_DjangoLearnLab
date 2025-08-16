from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginViews.as_view(template_name='blog/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutViews.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
