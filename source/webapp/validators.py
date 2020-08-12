from django.core.exceptions import ValidationError


def is_digit(string):
    if not string.isalpha():
        raise ValidationError('Header cannot contain numbers!')


def cennz(string):
    valid = ('mat', 'fack', 'han')
    for valids in valid:
        if valids in string:
            raise ValidationError('You used uncensored words')
