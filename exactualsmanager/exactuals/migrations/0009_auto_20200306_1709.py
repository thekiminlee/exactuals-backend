# Generated by Django 3.0.4 on 2020-03-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exactuals', '0008_auto_20200306_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='batch_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
