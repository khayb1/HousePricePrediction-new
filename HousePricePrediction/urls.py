"""
URL configuration for HousePricePrediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from .import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page URL
    path('home/', views.user_login, name='user_login'),  # User login URL
    path('register/', views.user_register, name='user_register'),  # User registration URL
    path('predict/', views.predict, name='predict'),  # Predict URL
    path('predict/result/', views.result, name='result'),  # Result URL
    path('predict/save_data/', views.save_data, name='save_data'),  # Save data URL
    path('predict/delete_row/<int:row_index>/', views.delete_row, name='delete_row'),  # Delete row URL
    path('home/', auth_views.LogoutView.as_view(), name='logout'), # Logout
]

