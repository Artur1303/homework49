from django.core.exceptions import ValidationError


def at_least_int(string):
    if str(string) == 10:
        raise ValidationError('This value is too short!')

def cennz(string):
    valid = ('mat', 'fack', 'han')
    for valids in valid:
        if string == valids:
            raise ValidationError('You used a bad word in the description')