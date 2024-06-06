from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def test_create_user(self):
        user = {
            "username": "mauro2",
            "email": "mauro2@gmail.com",
            "password": "ma@2909_pe"
        }

        response = self.client.post('/api/users', user, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        user = {
            "username": "mauro",
            "email": "mauro@gmail.com",
            "password": "ma@2909_pe"
        }

        self.client.post('/api/users', user, format="json")

        response = self.client.post('/api/token/', user, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_empty_username_create_user(self):
        user = {
            "username": "",
            "email": "mauro@gmail.com",
            "password": "ma@2909_pe"
        }

        response = self.client.post('/api/users', user, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_short_pass_create_user(self):
        user = {
            "username": "mauro",
            "email": "mauro@gmail.com",
            "password": "09_pe"
        }

        response = self.client.post('/api/users', user, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
