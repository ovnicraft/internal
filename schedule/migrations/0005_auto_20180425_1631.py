# Generated by Django 2.0.4 on 2018-04-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20180425_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date_end',
            field=models.DateField(null=True, verbose_name='Fecha Fin'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_start',
            field=models.DateField(null=True, verbose_name='Fecha Inicio'),
        ),
    ]
