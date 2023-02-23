from django.db import models
from django.utils import timezone

# Create your models here.


class Tareas(models.Model):
    # Field name made lowercase.
    idTarea = models.AutoField(db_column='idTarea', primary_key=True)
    title = models.TextField()
    created_at = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        'Opciones', models.DO_NOTHING, db_column='status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareasApi_tareas'


class Opciones(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Field name made lowercase.
    opsnombre = models.TextField(db_column='opsNombre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Opciones'
