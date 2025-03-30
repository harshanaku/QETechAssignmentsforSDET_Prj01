from django.test import TestCase, Client
from django.urls import reverse
import json

class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_home_page_loads(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_get_user_list(self):
        response = self.client.get(self.home_url, {'option': 'GET USER LIST'})
        self.assertEqual(response.status_code, 200)

    def test_get_single_user_not_found(self):
        response = self.client.get(self.home_url, {'option': 'GET SINGLE USER NOT FOUND'})
        self.assertEqual(response.status_code, 200)

    def test_post_create_user(self):
        response = self.client.post(self.home_url, {'option': 'POST CREATE USER', 'name': 'Jane Doe', 'job': 'Developer'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Jane Doe', response.content.decode())