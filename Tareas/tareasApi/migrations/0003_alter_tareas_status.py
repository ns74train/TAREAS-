# Generated by Django 4.1.5 on 2023-02-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareasApi', '0002_rename_id_tareas_idtarea_alter_tareas_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='status',
            field=models.CharField(choices=[('1', 'Realizado'), ('2', 'No Realizado'), ('3', 'En Proceso')], default='1', max_length=1),
        ),
    ]