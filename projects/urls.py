from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

urlpatterns = [
        url(r'^projects/$', views.ProjectList.as_view()),
        url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/?(P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
