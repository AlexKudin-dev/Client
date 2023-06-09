# Generated by Django 3.2.16 on 2023-01-18 05:56

from django.db import migrations, models
import utils.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Фотография')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Фамилия')),
                ('role_in_the_project', models.TextField(null=True, verbose_name='Роль в проекте')),
            ],
            options={
                'verbose_name': 'Друг',
                'verbose_name_plural': 'Друзья',
            },
            bases=(models.Model, utils.mixins.ReprMixin),
        ),
    ]
