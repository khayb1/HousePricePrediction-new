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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('predict/', views.predict, name ='predict'),
    path('predict/result', views.result, name='result'),
    path('predict/save_data', views.save_data, name='save_data' ),
    path('predict/delete_row/<int:row_index>/', views.delete_row, name='delete_row'),
    
]
