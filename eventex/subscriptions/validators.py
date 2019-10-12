from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('Cpf deve conter apenas numeros')

    if len(value)!=11:
        raise ValidationError('CPF deve ter 11 numeros.')