# Generated by Django 2.1.7 on 2019-03-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_auto_20190330_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/avatars'),
        ),
    ]
