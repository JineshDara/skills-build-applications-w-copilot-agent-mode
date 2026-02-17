
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import UserProfile

class UserProfileAPITests(APITestCase):
	def setUp(self):
		self.user = UserProfile.objects.create_user(username='testuser', email='test@example.com', password='testpass')

	def test_list_users(self):
		url = reverse('userprofile-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('results' in response.data or isinstance(response.data, list))

	def test_create_user(self):
		url = reverse('userprofile-list')
		data = {'username': 'newuser', 'email': 'new@example.com', 'password': 'newpass'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 201)
