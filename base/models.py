import datetime

from django.db import models


class AcademicCenter(models.Model):

    name = models.CharField('Centro Academico', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Centro Academico'
        verbose_name_plural = 'Centros Academicos'


class AcademicAnnouncement(models.Model):

    YEARS = []

    def year_choices():
        self.YEARS = [(r,r) for r in range(2000, datetime.date.today().year+1)]
        return years

    def current_year():
        return datetime.date.today().year

    year_start = models.IntegerField(
        verbose_name='Año Inicial',
        choices=YEARS,
        default=current_year)
    year_end = models.IntegerField(
        verbose_name='Año Final',
        choices=YEARS,
        default=current_year
    )

    def __str__(self):
        return '{0} - {1}'.format(self.year_start, self.year_end)

    class Meta:
        verbose_name = 'Convocatoria'
        verbose_name_plural = 'Convocatorias'


class AcademicCycle(models.Model):

    name = models.CharField('Ciclo de Estudio', max_length=128, default='*')
    date_start = models.DateField(verbose_name='Fecha Inicio')
    date_end = models.DateField(verbose_name='Fecha Fin')
    annoncement = models.ForeignKey('AcademicAnnouncement', on_delete=models.PROTECT)

    def __str__(self):
        return '[{0} - {1}] {2}'.format(self.date_start, self.date_end, self.annoncement)

    class Meta:
        verbose_name = 'Ciclo de Estudio'
        verbose_name_plural = 'Ciclos de Estudio'


class AcademicProgram(models.Model):

    name = models.CharField('Programa', max_length=128)
    center = models.ForeignKey(
        'AcademicCenter',
        on_delete=models.PROTECT,
        verbose_name='Centro Academico'
    )
    annoncement = models.ForeignKey(
        'AcademicAnnouncement',
        on_delete=models.PROTECT,
        verbose_name='Convocatoria'
    )
    date_start = models.DateField('Fecha Inicio')
    date_end = models.DateField('Fecha Fin')

    def __str__(self):
        return '[{1}] {0}'.format(
            self.name,
            self.annoncement
        )

    class Meta:
        verbose_name = 'Programa Academico'
        verbose_name_plural = 'Programas Academicos'
