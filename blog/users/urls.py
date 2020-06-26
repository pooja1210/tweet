from django.urls import path
from django.contrib.auth import views as auth_views
from users import views 
from .views import (
    register,
    SearchView
   
)


urlpatterns = [
    path('register/', views.register, name='register-users'),
    path('login/', auth_views.LoginView
         .as_view(template_name='user_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_logout.html'), name='logout'),
    path('search/', views.SearchView, name='search'),
        
]