from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Alisson Bittencourt',
                    cpf='12345678901',
                    email='alisson@teste.com',
                    phone='45-12345-6789')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscrition_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscrition_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscrition_email_to(self):
        expect = ['contato@eventex.com.br', 'alisson@teste.com']
        self.assertEqual(expect, self.email.to)


    def test_subscrition_email_body(self):
        contents = ['Alisson Bittencourt',
                    '12345678901',
                    'alisson@teste.com',
                    '45-12345-6789',
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
