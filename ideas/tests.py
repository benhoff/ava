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

    def test_authenticated_user_can_make_idea(self):
        url = reverse('idea-list')
        self.client.force_authenticate(user=self.user)
        data = {'project' : self.project,
                'description' : "descriptive description",
                'votes' : 1}

        response = self.client.post(url, data=data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

