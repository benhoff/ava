from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from projects.views import ProjectViewSet
from projects.models import Project

class ProjectTests(APITestCase):
    EXAMPLE_TEST_DATA = {"title":"test", 
                         "description":"really, test",
                         "status":"IDEA"}

    def setUp(self):
        self.user = User.objects.create_user(username='Rocket', password='foobar')
        self.user2 = User.objects.create_user('Bobby', password='foobar')

        # login user1
        self.client.login(username="Rocket", password='foobar')
        self.project = Project(owner=self.user, 
                               title='testing', 
                               description='Super test', 
                               status="IDEA") 

        self.project.save()

    def tearDown(self):
        self.user.delete()
        self.project.delete()

    def test_correct_user_can_patch_project(self):
        """
        This test ensures that project owners can make edits
        """
        data_dict = {'pk': self.project.pk}
        url = reverse('project-detail', kwargs=data_dict)
        self.client.force_authenticate(user=self.user)
        data = {"title":"updated_title"}
        response = self.client.patch(url, data=data, application='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'updated_title')

    def test_random_user_cannot_patch_random_projects(self):
        """
        This test ensures that random users can't edit project details
        """
        data_dict = {'pk': self.project.pk}
        url = reverse('project-detail', kwargs=data_dict)
        self.client.force_authenticate(self.user2)
        data = {"title" : "updated_title"}
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_project_detail_has_expected_parameters(self):
        """
        Tests that the JSON response project detail has all of the data that we expect
        """
        data_dict = {'pk': self.project.pk}
        url=reverse('project-detail',kwargs=data_dict)
        response = self.client.get(url, format='json')
    
        self.assertContains(response, 'url')
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertContains(response, 'user')
        self.assertContains(response, 'ownername')
        self.assertContains(response, 'owner_url')
        self.assertContains(response, 'status')
        self.assertContains(response, 'ideas')

    def test_project_list_has_expected_parameters(self):
        """
        Tests that the JSON response of the project list has all the data we expect
        """
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertContains(response, 'user')
        self.assertContains(response, 'ownername')
        self.assertContains(response, 'owner_url')
        self.assertContains(response, 'status')

    def test_get_project_detail(self):
        """
        Tests that we can get the project
        """
        data_dict = {'pk': self.project.pk}
        url = reverse('project-detail', kwargs=data_dict)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_detail_logged_out_user(self):
        """
        This tests makes sure that unautheticated users can read projects
        """
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
        self.client.force_authenticate(user=self.user)
        self.EXAMPLE_TEST_DATA['owner'] = '/users/{}/'.format(self.user2.pk)
        response = self.client.post(url,
                                    data=self.EXAMPLE_TEST_DATA,
                                    format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ownername'], self.user.username)

    def test_create_project_with_authenticated_user(self):
        """
        This tests that a authenticated user can make a project
        """
        url = reverse('project-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url,
                                    data=self.EXAMPLE_TEST_DATA,
                                    format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_project_list(self):
        """
        This test checks to see if we can get a project list
        """
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_list_with_logged_out_user(self):
        """
        This test checks to see if a logged out user can see the project list
        """
        url = reverse('project-list')
        self.client.logout()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
