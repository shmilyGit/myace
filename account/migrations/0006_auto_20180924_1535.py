# Generated by Django 2.1.1 on 2018-09-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_userinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
