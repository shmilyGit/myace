# Generated by Django 2.1.1 on 2018-11-06 22:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otrest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OtRest',
            new_name='OtRequest',
        ),
    ]
