from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_field(self):
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected,list(self.form.fields))


    def test_cpf_is_digit(self):
        data = dict(name='Alisson bittencourt',
                    cpf='abc45678901',
                    email='alison_btt@hotmail.com',
                    phone='45-99929-4016')

        form = SubscriptionForm(data)
        form.is_valid()

        self.assertListEqual(['cpf'], list(form.errors))


    def test_cpf_has_11_digits(self):
        data = dict(name='Alisson bittencourt',
                    cpf='45678901',
                    email='alison_btt@hotmail.com',
                    phone='45-99929-4016')

        form = SubscriptionForm(data)
        form.is_valid()

        self.assertListEqual(['cpf'], list(form.errors))