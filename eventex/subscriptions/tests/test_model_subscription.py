from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Alisson Bittencourt',
            cpf = '12345678901',
            email = 'alison@eventex.com',
            phone = '21-1234-1258'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at,datetime)

    def test_str(self):
        self.assertEqual('Alisson Bittencourt', str(self.obj))

    def test_paid_default_to_false(self):
        self.assertEqual(False, self.obj.paid)