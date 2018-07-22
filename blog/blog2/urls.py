"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from .views import *
from django.urls import path


app_name = 'blog2'
urlpatterns = [

    # Example: /
    path('', PostLV.as_view(), name="index"),

    # Example: /post/ (Same as /)
    path('post/', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    path('post/<slug:slug>/', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    path('archive/', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10
    path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    path('today/', PostTAV.as_view(), name='post_today_archive'),
]
