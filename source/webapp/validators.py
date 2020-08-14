from django.core.exceptions import ValidationError


def is_digit(string):
    valid = ('1', '2', '3', '4', '5', '6','7 ','8', '9', '0')
    for valids in valid:
        if string[0] in valids:
            raise ValidationError('Title cannot start with a number')



def cennz(string):
    valid = ('mat', 'fack', 'han')
    for valids in valid:
        if valids in string:
            raise ValidationError('You used uncensored words')
