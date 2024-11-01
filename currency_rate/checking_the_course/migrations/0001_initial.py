# Generated by Django 5.1.2 on 2024-10-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='СourseRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время запроса')),
                ('rate', models.FloatField(verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Запрос курса валюты',
                'verbose_name_plural': 'Список курсов валют',
                'ordering': ('-request_date',),
            },
        ),
    ]
