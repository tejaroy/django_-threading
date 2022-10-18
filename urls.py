"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from Apps.App import views

urlpatterns = [
    path('',views.home, name='home'),
    path('email', views.email, name='email'),
    path('empdata', views.empdata, name='empdata'),
    path('update_data/<int:id>', views.update_data, name='update_data'),
    path('delete_data/<int:id>', views.delete_data, name='delete_data'),
]



# #urls.py
# from django.urls import path
# from . import views
# from django.views.generic.base import TemplateView
# from demoapp.views import *
# urlpatterns = [
#         path('email', views.email, name='email'),
#     path('empdata', views.empdata, name='empdata'),
#     path('update_data/<int:id>', views.update_data, name='update_data'),
#     path('delete_data/<int:id>', views.delete_data, name='delete_data'),
# ]