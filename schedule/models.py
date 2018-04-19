from django.db import models


class Room(models.Model):

    name = models.CharField('Aula', max_length=64)

    def __str__(self):
        return self.name


class Schedule(models.Model):

    DAYS = [
        ('lunes', 'LUNES'),
        ('martes', 'MARTES'),
        ('miercoles', 'MIERCOLES'),
        ('jueves', 'JUEVES'),
        ('viernes', 'VIERNES'),
        ('sabado', 'SABADO'),
    ]

    asignatura = models.ForeignKey('asignatura.Materia', on_delete=models.PROTECT)
    teacher = models.ForeignKey('docente.Docente', on_delete=models.PROTECT)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    day = models.CharField('Día', choices=DAYS, max_length=32, default='lunes')
    hour_start = models.TimeField(verbose_name='Hora Inicio')
    hour_end = models.TimeField(verbose_name='Hora Salida')
    annoncement = models.ForeignKey('base.AcademicAnnouncement', on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey('base.AcademicProgram', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} {1}'.format(
            self.asignatura,
            self.annoncement
        )

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
