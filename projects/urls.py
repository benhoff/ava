from django.conf.urls import url, include
from projects import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)

# API endpoints
urlpatterns = [
        url(r'^$', include(router.urls)),

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
