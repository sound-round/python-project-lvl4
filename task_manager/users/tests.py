from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class UsersTest(TestCase):

    client = Client()

    def setUp(self):
        user = {
            'username': 'mark',
            'password1': 'secret-12345',
            'password2': 'secret-12345',
        }
        return self.client.post('/users/create/', user)

    def test_user_read(self):
        user = User.objects.get(username='mark')
        self.assertTrue(isinstance(user, User))
        self.assertEqual('mark', user.username)

    def test_user_update(self):
        user = User.objects.get(username='mark')
        user_id = user.id
        update_data = {'username': 'john'}
        response = self.client.post(f'/users/{user_id}/update/', update_data)
        user = User.objects.get(id=user_id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual('john', user.username)

    def test_user_delete(self):
        user = User.objects.get(username='mark')
        user_id = user.id
        response = self.client.post(f'/users/{user_id}/delete/')
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 302)
