from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ideas.tests import _BaseIdeaTest
from comments.models import Comment

class CommentTests(_BaseIdeaTest):

    def setUp(self):
        super(CommentTests, self).setUp()
        self.comment = Comment(content="This is commenty comment",
                               owner=self.user,
                               idea=self.idea)
        self.comment.save()

    def tearDown(self):
        super(CommentTests, self).tearDown()
        self.comment.delete()

    def test_comment_view_contains_expected_information(self):
        url = reverse('comment-detail', kwargs={'pk':self.comment.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'content')
        self.assertContains(response, 'owner')
        self.assertContains(response, 'idea')

