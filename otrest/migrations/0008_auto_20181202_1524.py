# Generated by Django 2.1.1 on 2018-12-02 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otrest', '0007_auto_20181129_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otrecord',
            name='otrequest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rn_OtRequest', to='otrest.OtRequest'),
        ),
    ]
