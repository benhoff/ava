from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

urlpatterns = patterns('', 
    url(r'^', include('projects.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('comments.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls', 
        namespace='rest_framework')),
)
