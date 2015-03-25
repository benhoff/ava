from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from projects.models import Project
from ideas.views import IdeaViewSet
from ideas.models import Idea

class IdeaTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('bob', password='foobar')
        self.project = Project(owner=self.user,
                                title='testing',
                                description='Super test',
                                status='IDEA')

        self.project.save()
        self.client.login(username='bob', password='foobar')
        self.IDEA_DATA = {'owner': self.user,
                            'title' : 'really descriptive title',
                            'project' : self.project,
                            'description': 'test idea',
                            'votes': 1}

        self.idea = Idea(**self.IDEA_DATA)
        self.idea.save()

    def test_idea_detail_view(self):
        d = {'pk' : self.idea.pk}
        url = reverse('idea-detail', kwargs=d)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_that_authenticated_user_can_patch_ideas(self):
        url = reverse('idea-detail', kwargs={'pk':self.idea.pk})
        response = self.client.patch(url, 
                                     data={'description': 'Look, a new description'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Look, a new description')

    def test_that_unauthenictaed_user_cannot_patch_ideas(self):
        url = reverse('idea-detail', kwargs={'pk': self.idea.pk})
        self.client.logout()
        response = self.client.patch(url,
                                     data={'description' : 'A'})
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_that_not_owner_cant_edit_ideas(self):
        user2 = User.objects.create_user('jimmy', password='foobar')
        self.client.logout()
        self.client.login(username='jimmy', pasword='foobar')
        url = reverse('idea-detail', kwargs={'pk': self.idea.pk})
        response = self.client.patch(url,
                                     data={'description':'B'})
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_make_idea(self):
        url = reverse('idea-list')
        data = {'project' : reverse('project-detail', 
                                    kwargs={'pk' : self.project.pk}),

                'description' : "descriptive description",
                'votes' : 1,
                'title' : 'second title'}

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_idea_detail_view_for_expected_params(self):
        url = reverse('idea-detail', kwargs={'pk': self.idea.pk})
        response = self.client.get(url)

        self.assertContains(response, 'url')
        self.assertContains(response, 'description')
        self.assertContains(response, 'votes')
        self.assertContains(response, 'username')
        self.assertContains(response, 'user_link')
        self.assertContains(response, 'created')
        self.assertContains(response, 'edited')
        self.assertContains(response, 'project')
        self.assertContains(response, 'title')


    def test_idea_list_view_for_expected_params(self):
        url = reverse('idea-list')
        response = self.client.get(url)

        self.assertContains(response,'url')
        self.assertContains(response, 'project')
        self.assertContains(response,'description')
        self.assertContains(response,'votes')
        self.assertContains(response,'username')
        self.assertContains(response,'user_link')
        self.assertContains(response, 'title')
