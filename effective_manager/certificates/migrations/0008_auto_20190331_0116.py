# Generated by Django 2.1.7 on 2019-03-31 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0007_auto_20190330_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'New'), (2, 'Assigned to poller'), (3, 'Poll done'), (4, 'Assigned to certificator'), (5, 'Certificate done'), (6, 'Certificate verified'), (7, 'Ended')], default=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='certificate_code',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]