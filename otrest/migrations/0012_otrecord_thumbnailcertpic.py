# Generated by Django 2.1.1 on 2019-08-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrest', '0011_auto_20190730_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='otrecord',
            name='thumbnailCertPic',
            field=models.ImageField(blank=True, upload_to='thumb'),
        ),
    ]