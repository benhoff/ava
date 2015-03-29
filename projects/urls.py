from django.conf.urls import url, include
from projects import views
import ideas.views
from rest_framework import routers

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

ideas_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
ideas_router.register(r'ideas', ideas.views.IdeaViewSet)


# The API URLS are now determine automatically by the router.
# Additionally, we include the login URLS for the browsable API.
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^', include(ideas_router))
]
