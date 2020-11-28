# Generated by Django 2.2.14 on 2020-11-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('schedule', models.DateTimeField()),
                ('estudiantes', models.ManyToManyField(related_name='materia', to='estudiantes.Estudiante')),
            ],
        ),
    ]
