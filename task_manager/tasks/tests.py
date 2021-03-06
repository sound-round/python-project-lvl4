from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TasksTest(TestCase):

    client = Client()

    def setUp(self):
        user1 = {
            'username': 'mark',
            'password1': 'secret-12345',
            'password2': 'secret-12345',
        }
        user2 = {
            'username': 'john',
            'password1': 'secret-12345',
            'password2': 'secret-12345',
        }
        status = {"name": "new"}

        self.client.post('/users/create/', user1)
        self.client.post('/users/create/', user2)
        self.client.login(username='mark', password='secret-12345')
        self.client.post('/statuses/create/', status)

        executor = User.objects.get(username='john')
        status = Status.objects.get(name='new')
        self.status = status
        task = {
            'name': 'Feature',
            'description': 'test description',
            'status': status.id,
            'executor': executor.id,
        }

        return self.client.post('/tasks/create/', task)

    def test_task_read(self):
        task = Task.objects.get(name="Feature")
        self.assertTrue(isinstance(task, Task))
        self.assertEqual('test description', task.description)
        self.assertEqual('mark', task.author.username)

    def test_task_update(self):
        task = Task.objects.get(name="Feature")
        task_id = task.id
        update_data = {
            'description': 'Updated description',
            'status': self.status.id,
            }
        response = self.client.post(
            f'/tasks/{task_id}/update/', update_data
        )
        task = Task.objects.get(id=task_id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(task.description, 'Updated description')

    def test_task_delete(self):
        task = Task.objects.get(name="Feature")
        task_id = task.id
        response = self.client.post(
            f'/tasks/{task_id}/delete/'
        )
        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(response.status_code, 302)
