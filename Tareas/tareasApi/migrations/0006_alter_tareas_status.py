# Generated by Django 4.1.5 on 2023-02-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareasApi', '0005_alter_tareas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='status',
            field=models.CharField(choices=[('1', 'Realizado'), ('2', 'No Realizado'), ('3', 'En Proceso')], default='Realizado', max_length=50),
        ),
    ]
