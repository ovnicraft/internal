from django.db import models


class Course(models.Model):

    def __str__(self):
        return '[{0}-{1}] {2}'.format(
            self.date_start,
            self.date_end,
            self.name
        )

    name = models.CharField(verbose_name='Curso Superior', max_length=128)
    date_start = models.DateField(verbose_name='Fecha Inicio')
    date_end = models.DateField(verbose_name='Fecha Fin')
    hours = models.IntegerField(verbose_name='Nro de Horas')
    teacher = models.ForeignKey('docente.Docente', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Curso Superior'
        verbose_name_plural = 'Cursos Superiores'
