# Generated by Django 2.1.1 on 2019-07-30 23:23

from django.db import migrations, models
import otrest.models


class Migration(migrations.Migration):

    dependencies = [
        ('otrest', '0010_auto_20190728_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otrecord',
            name='certPic',
            field=models.ImageField(blank=True, upload_to=otrest.models.user_directory_path),
        ),
    ]