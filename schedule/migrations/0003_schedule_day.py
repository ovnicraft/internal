# Generated by Django 2.0.4 on 2018-04-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20180418_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('lunes', 'LUNES'), ('martes', 'MARTES'), ('miercoles', 'MIERCOLES'), ('jueves', 'JUEVES'), ('viernes', 'VIERNES'), ('sabado', 'SABADO')], default='lunes', max_length=32, verbose_name='Día'),
        ),
    ]
