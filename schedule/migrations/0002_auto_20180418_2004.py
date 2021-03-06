# Generated by Django 2.0.4 on 2018-04-18 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20180418_1917'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='annoncement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.AcademicAnnouncement'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.AcademicProgram'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Room'),
        ),
    ]
