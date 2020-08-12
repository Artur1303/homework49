from django.core.exceptions import ValidationError


def is_digit(string):
    if not string.isalpha():
        raise ValidationError('Title cannot start with numbers!')


def cennz(string):
    valid = ('mat', 'fack', 'han')
    for valids in valid:
        if valids in string:
            raise ValidationError('You used a bad word in the description')