from django.conf.urls import url, include
from users import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

        url(r'^users/(?P<pk>[0-9]+)/$', views.RetrieveUserView.as_view(), name='user-detail')
]
