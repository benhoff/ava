from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

# API endpoints

urlpatterns = format_suffix_patterns([
        url(r'^$', views.api_root),
        url(r'^projects/$', 
            views.ProjectList.as_view(), 
            name='project-list'),

        url(r'^projects/(?P<pk>[0-9]+)/$', 
            views.ProjectDetail.as_view(),
            name='project-detail'),

        url(r'^projects/(?P<pk>[0-9]+)/highlights/$',
            views.ProjectHighlight.as_view(),
            name='project-highlight'),
        
        url(r'^users/$', 
            views.UserList.as_view(),
            name='user-list'),

        url(r'^users/?(P<pk>[0-9]+)/$', 
            views.UserDetail.as_view(),
            name='user-detail'),
])

urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework'))
]                           
