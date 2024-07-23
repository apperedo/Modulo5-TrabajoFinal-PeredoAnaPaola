from django.core.exceptions import ValidationError
import datetime as dt

def validar_vencimiento(value):
    if value < dt.date.today():
        raise ValidationError(
            '%(value)s no puede ser una fecha pasada',
            params={'value': value},
        )

def validar_descto(value):
    if value < 0:
        raise ValidationError(
            'El descuento no puede ser negativo (%(value)s)',
            params={'value': value},
        )
