import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient

from projects.views import ProjectViewSet
from projects.models import Project

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
        self.project.delete()

    """
    def test_expected_future_implementations(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertContains(response, 'username')

    def test_cant_edit_from_project_list(self):
        url = reverse('project-list')
        self.client.force_authenticate(user=self.user)
        self.assertEqual("Fix me", False)
    """

    def test_correct_user_can_patch_project(self):
        data_dict = {'pk': self.project.pk}
        url = reverse('project-detail', kwargs=data_dict)
        self.client.force_authenticate(user=self.user)
        data = {"title":"updated_title"}
        response = self.client.patch(url, data=data, application='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.project.title, 'updated_title')

    def test_project_detail_has_expected_parameters(self):
        """
        Tests that the JSON response has all of the data that we expect
        """
        data_dict = {'pk': self.project.pk}
        url=reverse('project-detail',kwargs=data_dict)
        response = self.client.get(url, format='json')
    
        self.assertContains(response, 'url')
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertContains(response, 'user')
    
    def test_project_list_has_expected_parameters(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')

        self.assertContains(response, 'url')
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertContains(response, 'user')

        self.assertContains(response, 'status')

    def test_get_project_detail(self):
        data_dict = {'pk': self.project.pk}
        url = reverse('project-detail', kwargs=data_dict)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_detail_logged_out_user(self):
        data_dict = {'pk': self.project.pk}
        url = reverse('project-detail', kwargs=data_dict)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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
    
    def test_create_project_authenticated_user_bogus_user_value(self):
        """
        This test checks to see if we can pass in a bogus user that isn't the user calling the method
        """
        url = reverse('project-list')
        user2 = User.objects.create_user('Bobby', password='foobar')
        self.client.force_authenticate(user=self.user)
        self.EXAMPLE_TEST_DATA['user'] = '/users/{}/'.format(user2.pk)

        response = self.client.post(url,
                                    data=self.EXAMPLE_TEST_DATA,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_project_with_authenticated_user(self):
        url = reverse('project-list')
        self.client.force_authenticate(user=self.user)
        self.EXAMPLE_TEST_DATA['user'] = '/users/{}/'.format(self.user.pk)
        response = self.client.post(url,
                                    data=self.EXAMPLE_TEST_DATA,
                                    format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_serializer_view(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_view_with_logged_out_user(self):
        url = reverse('project-list')
        self.client.logout()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
