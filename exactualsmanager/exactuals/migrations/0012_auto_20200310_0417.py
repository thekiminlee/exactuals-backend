# Generated by Django 3.0.4 on 2020-03-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exactuals', '0011_auto_20200310_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exactuals.User'),
        ),
    ]
