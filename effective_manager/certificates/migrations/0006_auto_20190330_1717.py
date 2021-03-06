# Generated by Django 2.1.7 on 2019-03-30 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0005_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='poller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poller', to=settings.AUTH_USER_MODEL),
        ),
    ]
