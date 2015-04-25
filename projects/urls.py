from django.conf.urls import url, include
import rest_framework.routers as rfr

# nrfr -> nested rest framework routers
import rest_framework_nested.routers as nrfr

from projects import views

import ideas.views as idea_view
import discussions.views as discussion_view
import problems.views as problem_view
import blog.views as blog_view


# Create a router and register our viewsets with it.
router = rfr.SimpleRouter()
router.register(r'projects', views.ProjectViewSet)

ideas_router = nrfr.NestedSimpleRouter(router, r'projects', lookup='project')
ideas_router.register(r'ideas', idea_view.IdeaViewSet)

discussion_router = nrfr.NestedSimpleRouter(router, r'projects', lookup='project')
discussion_router.register(r'discussions', discussion_view.DiscussionViewSet)

problem_router = nrfr.NestedSimpleRouter(router, r'projects', lookup='project')
problem_router.register(r'problems', problem_view.ProblemViewSet)

blog_router = nrfr.NestedSimpleRouter(router, r'projects', lookup='project')
blog_router.register(r'blog_posts', blog_view.PostViewSet)

# The API URLS are now determine automatically by the router.
# Additionally, we include the login URLS for the browsable API.
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^', include(ideas_router.urls)),
        url(r'^', include(discussion_router.urls)),
        url(r'^', include(problem_router.urls)),
        url(r'^', include(blog_router.urls)),
]
