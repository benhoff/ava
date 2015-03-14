from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ava.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('projects.urls')),
    url(r'^',include('users.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framewor    k')),
    url(r'^admin/', include(admin.site.urls)),
)
