from django.test import TestCase
from django.test import Client
from task_manager.statuses.models import Status


class StatusesTest(TestCase):

    client = Client()

    def set_up(self):
        status = {"name": "new"}
        user = {
            'username': 'mark',
            'password1': 'secret-12345',
            'password2': 'secret-12345',
        }
        self.client.post('/users/create/', user)
        self.client.login(username='mark', password='secret-12345')
        return self.client.post('/statuses/create/', status)

    def test_status_create(self):
        response = self.set_up()
        status = Status.objects.get(name="new")
        self.assertTrue(isinstance(status, Status))
        self.assertEqual(response.status_code, 302)
        self.assertEqual('new', status.name)

    def test_status_update(self):
        self.set_up()
        status = Status.objects.get(name="new")
        status_id = status.id
        update_data = {'name': 'done'}
        response = self.client.post(
            f'/statuses/{status_id}/update/', update_data
        )
        status = Status.objects.get(id=status_id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(status.name, 'done')

    def test_status_delete(self):
        self.set_up()
        status = Status.objects.get(name="new")
        status_id = status.id
        response = self.client.post(
            f'/statuses/{status_id}/delete/'
        )
        self.assertEqual(Status.objects.count(), 0)
        self.assertEqual(response.status_code, 302)
