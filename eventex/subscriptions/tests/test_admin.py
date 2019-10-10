from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionAdminTest(TestCase):
    def test_has_action(self):
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        Subscription.objects.create(name='Alisson Bittencourt',
                                    cpf='12345678901',
                                    email='alison_btt@hotmail.com',
                                    phone='21-99929-4016')
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        queryset = Subscription.objects.all()
        model_admin.mark_as_paid(None, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())