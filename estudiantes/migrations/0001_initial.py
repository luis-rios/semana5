# Generated by Django 2.2.14 on 2020-11-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=True)),
                ('sex', models.CharField(max_length=15)),
                ('enrollment', models.IntegerField(default=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]