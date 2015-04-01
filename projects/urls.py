from django.conf.urls import url, include
from projects import views
import ideas.views
import rest_framework.routers as rfr

# nrfr -> nested rest framework routers
import rest_framework_nested.routers as nrfr

# Create a router and register our viewsets with it.
router = rfr.SimpleRouter()
router.register(r'projects', views.ProjectViewSet)

ideas_router = nrfr.NestedSimpleRouter(router, r'projects', lookup='project')
ideas_router.register(r'ideas', ideas.views.NestedIdeaViewSet)

# The API URLS are now determine automatically by the router.
# Additionally, we include the login URLS for the browsable API.
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^', include(ideas_router.urls))
]
