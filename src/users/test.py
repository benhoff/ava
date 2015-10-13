from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from users.views import RetrieveUserView

class UserTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Rocket", password="foobar")
        print(self.user.username)
        self.client.login(username=self.user.username, password="foobar")

    def tearDown(self):
        self.user.delete()

    def test_user_detail_view_has_expected_parameters(self):
        url = reverse('user-detail', kwargs={'pk':self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, 'username')
        self.assertContains(response, 'projects')
        self.assertContains(response, 'ideas')
        #self.assertContains(response, 'feed')
