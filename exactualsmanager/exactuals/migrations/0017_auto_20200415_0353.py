# Generated by Django 3.0.4 on 2020-04-15 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exactuals', '0016_auto_20200415_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payor_payee',
            name='payee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exactuals.Payee', to_field='uid'),
        ),
        migrations.AlterField(
            model_name='payor_payee',
            name='payor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exactuals.Payor', to_field='uid'),
        ),
    ]
