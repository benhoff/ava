from django.conf.urls import url, include
from comments import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
