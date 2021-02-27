# Generated by Django 2.1.2 on 2021-02-27 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos_prestamo_manejado_por_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cedula', models.IntegerField()),
                ('email', models.CharField(max_length=70)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
