from django.db import models


class Room(models.Model):

    name = models.CharField('Aula', max_length=64)

    def __str__(self):
        return self.name


class Schedule(models.Model):

    DAYS = [
        ('1lunes', 'LUNES'),
        ('2martes', 'MARTES'),
        ('3miercoles', 'MIERCOLES'),
        ('4jueves', 'JUEVES'),
        ('5viernes', 'VIERNES'),
        ('6sabado', 'SABADO'),
    ]

    asignatura = models.ForeignKey('asignatura.Materia', on_delete=models.PROTECT)
    teacher = models.ForeignKey('docente.Docente', on_delete=models.PROTECT)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    day = models.CharField('Día', choices=DAYS, max_length=32, default='lunes')
    hour_start = models.TimeField(verbose_name='Hora Inicio')
    hour_end = models.TimeField(verbose_name='Hora Salida')
    date_start = models.DateField(verbose_name='Fecha Inicio', null=True)
    date_end = models.DateField(verbose_name='Fecha Fin', null=True)
    annoncement = models.ForeignKey('base.AcademicAnnouncement', on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey('base.AcademicProgram', on_delete=models.SET_NULL, null=True)
    posted = models.BooleanField('Publicado ?', default=True)

    def __str__(self):
        return '{2}: {0} [{1}]'.format(
            self.asignatura,
            self.annoncement,
            self.program
        )

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
