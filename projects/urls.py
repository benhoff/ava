from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)

# API endpoints
urlpatterns = format_suffix_patterns([
        url(r'^$', include(router.urls)),

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])
