from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string

from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    #Send Email
    _send_email('Confirmação de Inscrição',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'],
                'subscriptions/subscription_email.txt',
                form.cleaned_data)
    Subscription.objects.create(**form.cleaned_data)
    messages.success(request, 'Incricão realizada com secesso!')

    return HttpResponseRedirect('/inscricao')



def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form':SubscriptionForm()})

def _send_email(subject, from_, to, template_name, context):
    bady = render_to_string(template_name, context)
    mail.send_mail(subject, bady, from_, [from_, to])
