from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class SmartBankTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')  # Make sure your urls.py name='register'
        self.login_url = reverse('login')        # name='login'
        self.create_account_url = reverse('create-account')  # name='create-account'

        self.user_data = {
            "username": "john_doe",
            "email": "john@example.com",
            "password": "password123",
            "role": "customer"
        }

        self.account_data = {
            "account_type": "savings",
            "balance": 1000
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['user']['username'], self.user_data['username'])

    def test_user_login(self):
        # Register user first
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {
            "username": self.user_data['username'],
            "password": self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data['token'])

        # Save token for next test
        self.access_token = response.data['token']['access']

    def test_create_account(self):
        # Register and login user first
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {
            "username": self.user_data['username'],
            "password": self.user_data['password']
        }
        login_response = self.client.post(self.login_url, login_data, format='json')
        token = login_response.data['token']['access']

        # Set authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        # Create account
        response = self.client.post(self.create_account_url, self.account_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['account']['account_type'], self.account_data['account_type'])

