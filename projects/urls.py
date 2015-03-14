from django.conf.urls import url, include
from projects import views
from ideas import urls
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

# The API URLS are now determine automatically by the router.
# Additionally, we include the login URLS for the browsable API.
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^/ideas/$', include('ideas.urls'))
]
