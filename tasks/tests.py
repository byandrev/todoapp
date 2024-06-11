from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from tasks.models import Task


class TaskTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username="john", email="foo@bar.com", password="testJh#12345")
        refresh = RefreshToken.for_user(cls.user)
        cls.token = refresh.access_token
        cls.task = Task.objects.create(
            name="Ejemplo", description="Descripcion...", user_id=cls.user
        )

    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.user.delete()

    def setUp(self):
        self.client.force_authenticate(user=self.user, token=self.token)

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/', format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_create_task(self):
        task = {
            "name": "My Task",
            "description": "My task description"
        }

        response = self.client.post('/api/tasks/', task, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_detail(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.task.name)

    def test_update_task(self):
        task = {
            "name": "Nuevo Titulo"
        }

        response = self.client.patch(f"/api/tasks/{self.task.id}/", task, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), task["name"])

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
