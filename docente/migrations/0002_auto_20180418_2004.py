# Generated by Django 2.0.4 on 2018-04-18 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contratodocente',
            options={'verbose_name': 'Tipo de Contrato', 'verbose_name_plural': 'Tipos de Contratos'},
        ),
        migrations.AlterModelOptions(
            name='docente',
            options={'verbose_name': 'Docente', 'verbose_name_plural': 'Docentes'},
        ),
        migrations.RemoveField(
            model_name='docente',
            name='subject',
        ),
        migrations.AlterField(
            model_name='contratodocente',
            name='contract',
            field=models.CharField(max_length=100, verbose_name='Tipo de Contrato'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docente.ContratoDocente', verbose_name='Tipo de Contrato'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='docente',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='APELLIDOS'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='name',
            field=models.CharField(max_length=100, verbose_name='NOMBRES'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Telef'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='teacher_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docente.TipoDocente', verbose_name='Docente'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='work_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docente.CategoriaDocente', verbose_name='Categoría'),
        ),
    ]
