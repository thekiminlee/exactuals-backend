# Generated by Django 3.0.4 on 2020-04-15 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exactuals', '0019_auto_20200415_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='payor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='payor_payee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AlterField(
            model_name='payee',
            name='uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exactuals.User'),
        ),
        migrations.AlterField(
            model_name='payor',
            name='uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exactuals.User'),
        ),
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
        migrations.AlterField(
            model_name='payor_payee',
            name='ppid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ppid',
            field=models.ForeignKey(on_delete=models.SET('Payor_payee removed'), to='exactuals.Payor_Payee'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
