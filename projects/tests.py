import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient

from projects.views import ProjectViewSet
from projects.models import Project

"""
factory = APIRequestFactory()
user = User.objects.get(pk='1')
view = ProjectViewSet()

request = factory.get('/project/')
force_authenticate(request, user=user)
response = view(request)
"""
user = User.objects.get(pk='1')

class ProjectTests(APITestCase):
    EXAMPLE_TEST_DATA = {"title":"test", 
                         "description":"really, test",
                         "status":"IDEA"}

    def setUp(self):
        self.user = User.objects.create_user(username='Rocket', password='foobar')
        self.client.login(username="Rocket", password='foobar')
        self.project = Project(user=self.user, title='testing', description='Super test', status="IDEA") 
        self.project.save()

    def tearDown(self):
        self.user.delete()

    def test_create_project_with_unauthenticated_user(self):
        """
        Want to make sure that an unautheticated user can't create a project
        """
        self.client.logout()
        url = reverse('project-list')
        response = self.client.post(url, 
                                    data=self.EXAMPLE_TEST_DATA, 
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_project_with_authenticated_user(self):
        url = reverse('project-list')
        self.client.force_authenticate(user=self.user)
        self.EXAMPLE_TEST_DATA['user'] = '/users/1/'
        response = self.client.post(url,
                                    data=self.EXAMPLE_TEST_DATA,
                                    format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # TODO: Figure out how to not explictly pass in the user

    def test_serializer_view(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
