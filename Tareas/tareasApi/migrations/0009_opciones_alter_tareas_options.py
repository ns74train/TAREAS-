# Generated by Django 4.1.5 on 2023-02-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareasApi', '0008_alter_tareas_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opciones',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('opsnombre', models.TextField(blank=True, db_column='opsNombre', null=True)),
            ],
            options={
                'db_table': 'Opciones',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='tareas',
            options={'managed': False},
        ),
    ]