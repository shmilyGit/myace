# Generated by Django 2.1.1 on 2019-08-02 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otrest', '0012_otrecord_thumbnailcertpic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otrecord',
            old_name='thumbnailCertPic',
            new_name='thumbCertPic',
        ),
    ]
