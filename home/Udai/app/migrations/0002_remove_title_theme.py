# Generated by Django 2.2.3 on 2019-07-18 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='Theme',
        ),
    ]
