"""saltshaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^all_group', views.all_group,name='all_group'),
    url(r'^ajaz_dict', views.ajax_dict,name='ajax_dict'),
    url(r'^ajax_list', views.ajax_list,name='ajax_list'),
    url(r'^del_group', views.del_group,name='del_group'),
    url(r'^add_group', views.add_group,name='add_group'),
    url(r'^modify_group', views.modify_group,name='modify_group'),
]