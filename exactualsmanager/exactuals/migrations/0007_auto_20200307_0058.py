# Generated by Django 3.0.3 on 2020-03-07 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exactuals', '0006_auto_20200307_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payor_payee',
            name='payee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exactuals.Payee'),
        ),
        migrations.AlterField(
            model_name='payor_payee',
            name='payor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exactuals.Payor'),
        ),
    ]
