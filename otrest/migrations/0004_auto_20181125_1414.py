# Generated by Django 2.1.1 on 2018-11-25 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otrest', '0003_auto_20181106_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateField(blank=True)),
                ('endTime', models.DateField(blank=True)),
                ('isCommit', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='otrequest',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='otrequest',
            name='ottime',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='otrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn_OtRequestUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='otrecord',
            name='otrequest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='otrest.OtRequest'),
        ),
        migrations.AddField(
            model_name='otrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn_OtRecordUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
