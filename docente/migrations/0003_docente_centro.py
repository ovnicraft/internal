# Generated by Django 2.0.4 on 2018-04-19 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20180418_1917'),
        ('docente', '0002_auto_20180418_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.AcademicCenter'),
        ),
    ]
