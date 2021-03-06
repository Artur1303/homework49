# Generated by Django 2.2 on 2020-09-13 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар')),
                ('profile_github', models.URLField(blank=True, max_length=100, null=True, verbose_name='Профиль  на гитхаб')),
                ('about_myself', models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='О себе')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'permissions': {('viewing_the_list_of_users', 'просмотр списока пользователей')},
            },
        ),
    ]
