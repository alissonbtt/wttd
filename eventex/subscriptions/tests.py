from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')


    def test_get(self):
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')


    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_has_form(self):
        form =self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_field(self):
        form = self.resp.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Alisson Bittencourt',
                    cpf='12345678901',
                    email='alisson@teste.com',
                    phone='45-12345-6789')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        '''Testar o Post de Dados do formulario e redirecionar para /inscricao'''
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))


    def test_subscrition_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, email.subject)

    def test_subscrition_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, email.from_email)


    def test_subscrition_email_to(self):
        email = mail.outbox[0]
        expect = ['contao@eventex.com.br', 'alisson@teste.com']
        self.assertEqual(expect, email.to)


    def test_subscrition_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Alisson Bittencourt', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('alisson@teste.com', email.body)
        self.assertIn('45-12345-6789', email.body)

class SubscribeInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/',{})

    def test_post(self):
        '''Para um Post Invalido nao sera redireciondo'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_erros(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)


class SubiscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Alisson Bittencourt',
                    cpf='12345678901',
                    email='alisson@teste.com',
                    phone='45-12345-6789')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Incricão realizada com secesso!')
