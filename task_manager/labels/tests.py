from django.test import TestCase
from django.test import Client
from task_manager.labels.models import Label


class LablesTest(TestCase):

    client = Client()

    def set_up(self):
        label = {"name": "new label"}
        user = {
            'username': 'mark',
            'password1': 'secret-12345',
            'password2': 'secret-12345',
        }
        self.client.post('/users/create/', user)
        self.client.login(username='mark', password='secret-12345')
        return self.client.post('/labels/create/', label)

    def test_label_create(self):
        response = self.set_up()
        label = Label.objects.get(name="new label")
        self.assertTrue(isinstance(label, Label))
        self.assertEqual(response.status_code, 302)
        self.assertEqual('new label', label.name)

    def test_label_update(self):
        self.set_up()
        label = Label.objects.get(name="new label")
        label_id = label.id
        update_data = {'name': 'updated label'}
        response = self.client.post(
            f'/labels/{label_id}/update/', update_data
        )
        label = Label.objects.get(id=label_id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(label.name, 'updated label')

    def test_label_delete(self):
        self.set_up()
        label = Label.objects.get(name="new label")
        label_id = label.id
        response = self.client.post(
            f'/labels/{label_id}/delete/'
        )
        self.assertEqual(Label.objects.count(), 0)
        self.assertEqual(response.status_code, 302)
