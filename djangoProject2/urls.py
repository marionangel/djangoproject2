"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from djangoProject2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='my-home'),
    path('About/',views.About,name='my-about'),
    path('Product/',views.Product,name='my-product'),
    path('Services/',views.Services,name='my-services'),
    path('Gallery/',views.Gallery,name='my-gallery'),
    path('Contact/',views.Contact,name='my-contact'),
]
