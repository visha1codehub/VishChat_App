# Generated by Django 4.2 on 2023-12-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
