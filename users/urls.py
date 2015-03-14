from django.conf.urls import url, include
from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserSerializer)

urlpatterns = [
        url(r'^/user', include(router.urls)),
]
