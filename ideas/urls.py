from django.conf.urls import url, include
from ideas import views
from comments import urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^', views.IdeaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^/comments/$', include('comments.urls'), name='comment-view'),
]
