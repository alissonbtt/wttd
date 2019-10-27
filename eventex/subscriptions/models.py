from django.db import models
from eventex.subscriptions.validators import validate_cpf
from django.shortcuts import resolve_url as r

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf  = models.CharField(max_length=11, validators=[validate_cpf])
    email  = models.EmailField(blank=True)
    phone  = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subscriptions:detail', self.pk)
