# Generated by Django 3.0.4 on 2020-03-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exactuals', '0012_auto_20200310_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='ppid',
            field=models.ForeignKey(db_column='ppid', on_delete=models.SET('Payor_payee removed'), to='exactuals.Payor_Payee', to_field='ppid'),
        ),
    ]
