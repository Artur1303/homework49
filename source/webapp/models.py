from django.db import models
from django.core.validators import MinLengthValidator
from webapp.validator import at_least_int, cennz


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Заголовок',validators=[MinLengthValidator(10)])
    descriptions = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание', validators=[cennz])
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, verbose_name='Статус')
    type =  models.ManyToManyField('webapp.Type',related_name='tasks', verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.summary}'